/*****************************************************************************
 * play_wavfile_sfread.c
 *
 * Plays a WAV file to speaker using PortAudio
 * Uses sndfile library calls in callback
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h> 	/* malloc() */
#include <unistd.h>     /* sleep() */
#include <stdbool.h>	/* true, false */
#include <string.h>		/* memset() */
#include <ctype.h>		/* lolower() */
#include <math.h>		/* sin() */
#include <sndfile.h>	/* libsndfile */
#include <portaudio.h>	/* portaudio */
#if (__APPLE__)
#include <stdatomic.h>  /* permits write/read of "slection" to be atomic */
#endif
#include "paUtils.h"

#define MAX_CHN	            2
#define FRAMES_PER_BUFFER   512 

/* data structure to pass to callback */
typedef struct {
#if (__APPLE__)
	atomic_int play;	/* so play variable is thread-safe */
#else
	int play;
#endif
	/* libsndfile data structures */
	SNDFILE *sndfile; 
	SF_INFO sfinfo;
} Buf;

/* PortAudio callback function protoype */
static int paCallback( const void *inputBuffer, void *outputBuffer,
	unsigned long framesPerBuffer,
	const PaStreamCallbackTimeInfo* timeInfo,
	PaStreamCallbackFlags statusFlags,
	void *userData );

int main(int argc, char *argv[])
{
  	char *ifile;
  	/* callback data structure */
  	Buf buf, *p = &buf;
  	/* PortAudio stream */
	PaStream *stream;

  	/* zero libsndfile structure */
	memset(&p->sfinfo, 0, sizeof(p->sfinfo));

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
	/* If number of channels > MAX_CHN, exit */

	p->sndfile  = sf_open(ifile, SFM_READ, &p -> sfinfo);

    	if(p->sndfile == NULL){
    		printf("Failed to open file '%s'.\n", ifile);
    		printf("%s\n", sf_strerror(NULL));
  		return 1;
    }

	printf("Sample rate: %d\n", p->sfinfo.samplerate);
	printf("Channels: %d\n", p->sfinfo.channels);
	printf("Frames: %lld\n", p-> sfinfo.frames);	
	printf("Format: %d\n", p-> sfinfo.format);
	


   	if(p -> sfinfo.channels > MAX_CHN){
   		fprintf(stderr, "Error: File '%s' has too many channels (found %d, max %d)\n", argv[1], 
        	p -> sfinfo.channels, MAX_CHN);
        	sf_close(p->sndfile);
        	return 1;
   }

	
	
	

	/* Initialize data structure 
	 * set play to 0 so initially only "zeros" are played
	 */
	p->play = 0;

	/* Start up Port Audio */
	stream = startupPa(1, p->sfinfo.channels, 
	    p->sfinfo.samplerate, FRAMES_PER_BUFFER, paCallback, &buf);

	/* Wait for user input 
	 * Enter 'Q' to quit or CR to toggle between play and pause
	 */
  	while (1) {
  		char line[80];
  		fgets (line, 80, stdin);
  		if (line[0] == 'Q')
  			break;
  		else 
  			p->play = (p->play==0) ? 1 : 0;
  	}

	/* Shut down Port Audio */
	shutdownPa(stream);
	 
	/* Close WAV file */
	sf_close(p->sndfile);
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
	float *output = (float *)outputBuffer;
	//float *input = (float *)inputBuffer; /* input not used in this code */
	int samplesPerBuffer = framesPerBuffer * p->sfinfo.channels; /* number or samples in buffer */
	int play, i, count;
 
	/* if play is 0, then fill output buffer with zeros
	 * otherwise, read from WAV file into callback output buffer
	 * if not enough samples (i.e. count < framesPerBuffer)
	 * then rewind WAV file and read remaining samples into output buffer
	 */

	play = p->play;
	if (play==0) {
		count = sf_readf_float(p->sndfile, output, framesPerBuffer);
		if ( count < framesPerBuffer) { 
			sf_seek(p->sndfile, 0, SEEK_SET); 
			sf_readf_float(p->sndfile, output + count*
				p->sfinfo.channels,(framesPerBuffer-count));
    	}
	} 
	else {
		for (i = 0; i < samplesPerBuffer; i++) {
        	*output++ = 0.0;
    }
}
	return 0;
}
