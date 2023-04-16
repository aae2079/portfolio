/*****************************************************************************
 * play_wavfile.c
 *
 * Plays a WAV file to speaker using PortAudio
 * Uses pointers to Wav buffer in callback
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h> 	/* malloc() */
#include <unistd.h>     /* sleep() */
#include <stdbool.h>	/* true, false */
#include <string.h>	/* memset() */
#include <ctype.h>	/* lolower() */
#include <math.h>	/* sin() */
#include <sndfile.h>	/* libsndfile */
#include <portaudio.h>	/* portaudio */
#if (__APPLE__)
#include <stdatomic.h>  /* permits write/read of "slection" to be atomic */
#endif
#include "paUtils.h"

#define MAX_CHN	            2
#define LINE_LEN			80
#define FRAMES_PER_BUFFER   1024 

/* data structure to pass to callback */
typedef struct {
#if (__APPLE__)
	atomic_int play;	/* so play variable is thread-safe */
#else
	int play;
#endif
	unsigned int channels;
	float *top;
	float *next;
	float *bottom;
} Buf;

/* PortAudio callback function protoype */
static int paCallback( const void *inputBuffer, void *outputBuffer,
	unsigned long framesPerBuffer,
	const PaStreamCallbackTimeInfo* timeInfo,
	PaStreamCallbackFlags statusFlags,
	void *userData );

int main(int argc, char *argv[]){
  	char *ifile;
  	/* my data structure */
  	Buf buf, *p = &buf;
  	/* libsndfile structures */
	SNDFILE *sndfile; 
	SF_INFO sfinfo;
  	/* PortAudio stream */
	PaStream *stream;

  	/* zero libsndfile structures */
	memset(&sfinfo, 0, sizeof(sfinfo));

  	/* 
  	 * Parse command line 
  	 */
	if(argc !=2 ){
		fprintf(stderr, "Usage: %s input_file\n", argv[0]);
		return -1;
	}

	ifile = argv[1];

	/* Open WAV file */
	/* Print information about WAV file */

	sndfile  = sf_open(ifile, SFM_READ, &sfinfo);

	if(sndfile == NULL){
    		printf("Failed to open file '%s'.\n", argv[1]);
    		printf("%s\n", sf_strerror(NULL));
  		return 1;
    }

    printf("Sample rate: %d\n", sfinfo.samplerate);
	printf("Channels: %d\n", sfinfo.channels);

	/* If number of channels > MAX_CHN, exit */
	if(sfinfo.channels > MAX_CHN){
   		fprintf(stderr, "Error: File '%s' has too many channels (found %d, max %d)\n", argv[1], 
        	sfinfo.channels, MAX_CHN);
        	sf_close(sndfile);
        	return 1;
        }
	/* malloc storage and read audio data into buffer 
	 * allocate storage to p->bottom 
	 */
	p->bottom = (float*)malloc(sizeof(float) * sfinfo.frames * sfinfo.channels);
	sf_readf_float(sndfile, p->bottom, sfinfo.frames);
	sf_close(sndfile);


	/* Initialize data structure 
	 * Set play to 0 so initially only "zeros" are played
	 */
	p->play = 0;
	/* Set channels */
	p->channels = sfinfo.channels;
	/* initialize pointers in WAV data struct 
	 * bottom already points to start of WAV data 
	 * next points to next frame to play out
	 * top points to last frame in buffer
	 */
	p->next = p->bottom;
	p->top = &p->bottom[(sfinfo.frames-1) * sfinfo.channels];

	

	/* Close WAV file */
	sf_close(sndfile);
	

	/* start up Port Audio */
	stream = startupPa(1, sfinfo.channels, sfinfo.samplerate, 
		FRAMES_PER_BUFFER, paCallback, &buf);

  	/* User Input */
  	while (1) {
  		char line[80];
  		fgets (line, 80, stdin);
  		if (line[0] == 'Q')
  			break;
  		else 
  			p->play = (p->play==0) ? 1 : 0;
  	}

	/* shut down Port Audio */
	shutdownPa(stream);

	/* free storage */
	free(p->bottom);

	return 0;
}


/* This routine will be called by the PortAudio engine when audio is needed.
 * It will be called in the "real-time" thread, so don't do anything
 * in the routine that requires significant time or resources.
 */
static int paCallback(const void *inputBuffer, void *outputBuffer,
	unsigned long framesPerBuffer,
	const PaStreamCallbackTimeInfo* timeInfo,
	PaStreamCallbackFlags statusFlags,
	void *userData)
{
	Buf *p = (Buf *)userData; /* Cast data passed through stream to our structure. */
	//float *input = (float *)inputBuffer; /* input not used in this code */
	float *po = (float *)outputBuffer;
	int samplesPerBuffer = framesPerBuffer * p->channels; /* number or samples in buffer */
	int play = p->play;
 
	/* if play is 0, then fill output buffer with zeros
	 * otherwise, copy from WAV data buffer into callback output buffer
	 * if not enough samples (i.e. p->next > p->top), then reset 
	 * pointer p->next to start of buffer and copy remaining samples into output buffer
	 * if using local pointers, update p->next before exiting
	 */
 
	if (play==0) {
		memset(po, 0, sizeof(float) * samplesPerBuffer);
		
} 	else {
	for (int i = 0; i < framesPerBuffer; i++) {
		for (int j = 0; j < p->channels; j++) {
				*po++ = *p->next++;
			}
		if (p->next + samplesPerBuffer >= p->top) {
			p->next = p->bottom;
		}
	}
		for (int i = 0; i < framesPerBuffer; i++) {
 			*po++ = 0;
		} 
	} 

	return 0;
}
