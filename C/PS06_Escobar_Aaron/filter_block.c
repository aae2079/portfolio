 /* FIR filtering of a WAV file in real-time (with playout) using block processing */

#include <stdio.h>
#include <stdlib.h>		//malloc()
#include <string.h>		//memset()
#include <unistd.h>		//sleep()
#include <stdbool.h>	//bool
#if __APPLE__
#include <stdatomic.h>	//atomic read/write
#endif
#include <sndfile.h>	//sndfile
#include <portaudio.h>	//portaudio
#include "paUtils.h"	//portaudio utility functions
#include "filter.h"	//declares struct Filt and State

/* instantiation of FIR filter struct */
struct FIR_Filt filt = {
	/* FIR filter length */
	191,
	/* b coefficients */
	{
#include "fir_filt_coef.h" //FIR filter coefficients
	}
};

#define BLK_LEN	1024	//block length for block processing

/* PortAudio callback structure */
struct PABuf {
	float *ifbuf;
	float *ofbuf;
	int frames;
	int channels;
	int next_frame;
#if __APPLE__
	atomic_bool done;
#else
	bool done;
#endif
	struct FIR_Filt *pf;
	float *ps;
};

/* PortAudio callback function protoype */
static int paCallback( const void *inputBuffer, void *outputBuffer,
    unsigned long framesPerBuffer,
    const PaStreamCallbackTimeInfo* timeInfo,
    PaStreamCallbackFlags statusFlags,
    void *userData );

int main(int argc, char *argv[])
{
	char *ifile, *ofile;
	float *ifbuf, *ofbuf;
	/* lib snd file */
    SNDFILE *isndfile, *osndfile;
    SF_INFO isfinfo, osfinfo;
	int count;
    /* port audio */
	struct PABuf paBuf;
    PaStream *stream;
    /* state for block processing */
	float state[MAX_COEF*MAX_CHAN];


	if(argc !=3 ){
		fprintf(stderr, "Usage: %s input_file output_file\n", argv[0]);
		return -1;
	}

	ifile = argv[1];

	ofile = argv[2];

	/* zero input file info */
	memset(&isfinfo, 0, sizeof(isfinfo));

    /* Open input and output files 
     * Print input file parameters
     */
	isndfile = sf_open(ifile,SFM_READ, &isfinfo);

	if(isndfile == NULL){
    		printf("Failed to open file '%s'.\n", ifile);
    		printf("%s\n", sf_strerror(NULL));
  		return 1;
    }
	printf("Sample rate: %d\n", isfinfo.samplerate);
	printf("Channels: %d\n", isfinfo.channels);

    /* Set output file parameters */
	osfinfo.samplerate = isfinfo.samplerate;
    osfinfo.channels = isfinfo.channels;
    osfinfo.format = isfinfo.format;

    /* Open output file */
	osndfile = sf_open(ofile,SFM_WRITE,&osfinfo);
	
	if(osndfile == NULL){
    		printf("Failed to open file '%s'.\n", ofile);
    		printf("%s\n", sf_strerror(NULL));
  		return 1;
    }

	/* Allocate input and output buffers and read input signal
	 * N is isfinfo.frames
	 * C is isfinfo.channels
	 * M is filt.num_b
	 * Input
	 * malloc storage ifbuf[] for N frames of C channels/frame
	 * Output
	 * malloc storage ofbuf[] for (N+M-1) frames of C channels/frame
	 */
    int N = isfinfo.frames;
    int C = isfinfo.channels;
    int M = filt.num_b;

    ifbuf = (float*)malloc(sizeof(float) * N*C);
    ofbuf = (float*)malloc(sizeof(float)* (N+M-1)*C);
	/* Read input WAV file into ifbuf */

    count = sf_read_float(isndfile,ifbuf,N*C);
    if (count != N * C) {
    	printf("Error reading input file %s\n", ifile);
    		exit(-1);
    }

	/* initialize Port Audio data struct */
	paBuf.ifbuf = ifbuf;
	paBuf.ofbuf = ofbuf;
	paBuf.frames = isfinfo.frames;
	paBuf.channels = isfinfo.channels;
	paBuf.next_frame = 0;
	paBuf.done = false;
	paBuf.pf = &filt;
	paBuf.ps = &state[0];
	/* zero state buffer */
	memset(state, 0, sizeof(state));

    /* start up Port Audio */
    printf("Starting PortAudio %d %d\n", 1, isfinfo.channels);
    stream = startupPa(1, isfinfo.channels, 
      isfinfo.samplerate, BLK_LEN, paCallback, &paBuf);

	/* 
	 * sleep and let callback process audio until done 
	 */
    while (!paBuf.done) {
    	printf("%d\n", paBuf.next_frame);
    	fflush(stdout); //Win32 needs this
    	sleep(1);
    }
	
	printf("Done\n");

    /* shut down Port Audio */
    shutdownPa(stream);
    
	/* Write output */
	
    count = sf_write_float(osndfile, ofbuf, (N+M-1)*C);
    if (count != (N+M-1) * C) {
		printf("Error writing output file %s\n", ofile);
    	exit(-1);
		}
	
	/* close WAV files 
	 * free allocated storage
	 */
    sf_close(isndfile);
    sf_close(osndfile);
    
    free(ifbuf);
    free(ofbuf);
    
	return 0;
}

static int paCallback(
	const void *inputBuffer, 
	void *outputBuffer,
    unsigned long framesPerBuffer,
    const PaStreamCallbackTimeInfo* timeInfo,
    PaStreamCallbackFlags statusFlags,
    void *userData)
{

    /* Cast data passed via paCallback to our struct */
    struct PABuf *p = (struct PABuf *)userData; 
    /* cast input and output buffers */
    //float *input = (float *)inputBuffer; //not used in this code
    float *output = (float *)outputBuffer;
	int N = framesPerBuffer;
	int C = p->channels;
	int M = p->pf->num_b; //number of FIR coefficients
	
	/* local pointers to ifbuf[] and ofbuf[] 
	 * these point to sample of first channel of next frame to process
	 */
    float *ifbuf = p->ifbuf + p->next_frame*C;
    float *ofbuf = p->ofbuf + p->next_frame*C;
    float *state = p->ps;
 	
 	/* pointer to FIR filter coefficients */
 	double *b = &(p->pf->b[0]);	

	/* zero PortAudio output buffer for:
	 * partial output buffer
	 * or call to PortAudio after done == true (after all input data has been processed)
	 */
	for (int i=0; i<N*C; i++) {
		output[i] = 0;
	}

	/* return if done */
	if (p->done == true) {
		 return 0;
	}

	/* adjust N if last frame is partial frame */
	if (p->next_frame + N > p->frames) {
		N = p->frames - p->next_frame;
	}

	/* filter input buffer and state buffer 
	 * to create output buffer
	 * 
	 * after filtering input buffer, 
	 * update state buffer
	 */
	
	/*
	float *x = &ifbuf[C]; 
    float *y = &ofbuf[C]; 
    float *s = p->ps; 
	*/
	
	for (int n = 0; n < N; n++) {
        double sum = 0;
		for (int k = 0; k < M; k++) { 
			if (n - k >= 0) {
				sum += ifbuf[n - k] * b[k]; 
			} else {
				sum += state[(M-1)+(n-k)] * b[k]; 
			}
		}
		ofbuf[n] = sum; 
	}
	
		
	//Copy last M-1 to state buffer (but OK to copy M) 
	
	for (int i=0; i<M-1; i++) {
		state[M-2-i] = ifbuf[(N*C-1)-i];
	}

	
	/* copy the current block portion of ofbuf[] 
	 * to portaudio output buffer 
	 */
	for (int i=0; i<N*C; i++) {
		output[i] = ofbuf[i];
	}
	
	/* increment next_frame counter */
	p->next_frame += N;
	/* check if done */
	if (p->next_frame >= p->frames) {
		p->done = true;
	}

	return 0;
}
