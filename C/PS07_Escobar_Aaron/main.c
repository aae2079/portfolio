/* Program for a sinewave generation synthesizer
 * which can play simultaneous tones
 * 
 * Demonstrates use of NCurses (if Mac) and PortAudio (also libsnd for debugging file) 
 */

#include <stdio.h>
#include<unistd.h>      /* sleep() */
#include <string.h>		/* memset() */
#include <sndfile.h>	/* libsndfile */
#include <stdbool.h>    /* type bool */
#include <portaudio.h>	/* portaudio */
#include <stdatomic.h>  /* permits write/read of "cmd" to be atomic */
#include "synth.h"      /* struct Synth */
#include "paUtils.h"    /* portaudio function prototypes */
#ifdef __APPLE__ 
#define USE_NCURSES
void user_io_ncurses(Synth *ps);
#else
#undef  USE_NCURSES
void user_io_plain(Synth *ps);
#endif

/* write output to wav file for debugging */
#define DB_WAV_OUT          0   

/* PortAudio callback function protoype */
static int paCallback( 
    const void *inputBuffer, 
    void *outputBuffer,
    unsigned long framesPerBuffer,
    const PaStreamCallbackTimeInfo* timeInfo,
    PaStreamCallbackFlags statusFlags,
    void *userData );

/* callback structure */
typedef struct {
    Synth *ps;
#if (DB_WAV_OUT)
    SNDFILE *sndfile;
#endif
} Buf;

int main(int argc, char *argv[])
{
    /* instantiate instance of Synth struct */
    Synth synth;
    Synth *ps = &synth;
	/* instantiate instance of portaudio callback data structure */
	Buf buf;
	/* PortAudio data stream */
    PaStream *stream;
#if (DB_WAV_OUT)
    /* libsndfile data structures */
    SF_INFO sfinfo;
#endif

    /* initialize Synth */
    init_synth(ps, NUM_CHAN, SAMP_RATE);
    sleep(2); //pause so key freq can be observed

    /* initialize struct for callback */
    buf.ps = ps;

    /* start up Port Audio */
    stream = startupPa(1, NUM_CHAN, 
        SAMP_RATE, FRAMES_PER_BUFFER, paCallback, &buf);

#if (DB_WAV_OUT)
    /* open debug output file */
    memset(&sfinfo, 0, sizeof(sfinfo));
    sfinfo.samplerate = SAMP_RATE;
	sfinfo.channels = NUM_CHAN;
	sfinfo.format = SF_FORMAT_WAV | SF_FORMAT_PCM_16;
    if ( (buf.sndfile = sf_open ("test_file.wav", SFM_WRITE, &sfinfo)) == NULL ) {
        fprintf (stderr, "Error: could not open test wav file\n");
        return -1;
    }
#endif

#ifdef USE_NCURSES 
    user_io_ncurses(ps);
#else
    user_io_plain(ps);
#endif

#if (DB_WAV_OUT)
    /* close debugging output wav file */
    sf_close (buf.sndfile);
#endif

    /* shut down Port Audio */
    shutdownPa(stream);

    return 0;
}


/* This routine will be called by the PortAudio engine when audio is needed.
 * It will be called in the "real-time" thread, so don't do anything
 * in the routine that requires significant time or resources.
 */
static int paCallback(
    const void *inputBuffer, 
    void *outputBuffer,
    unsigned long framesPerBuffer,
    const PaStreamCallbackTimeInfo* timeInfo,
    PaStreamCallbackFlags statusFlags,
    void *userData)
{
    Buf *pb = (Buf *)userData; /* Cast pointer to data passed through stream */
    Synth *ps = pb->ps;  /* struct Synth */
    float *output = (float *)outputBuffer;
    //float *input = (float *)inputBuffer; /* input not used in this code */

    /* synthesize tones */
    synth_block(ps, framesPerBuffer, output);

#if (DB_WAV_OUT)
    /* write to debugging file */
    sf_writef_float (pb->sndfile, output, framesPerBuffer);
#endif

    return 0;
}