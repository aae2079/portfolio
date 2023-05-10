#ifndef _SYNTH_H_
#define _SYNTH_H_

#include <stdbool.h>
#include <stdatomic.h>  /* permits write/read of "cmd" to be atomic */

/* other defines */
#define KEYS_VOICED         4   /* number of simultaneouse keys voiced */
#define SAMP_RATE           48000
#define NUM_CHAN	        2
#define FRAMES_PER_BUFFER   1024
#define FS_AMPL             0.5 /* -6 dB FS */
#define ATTACK_FACTOR       0.99800 /* attack time constant of 10 ms */
#define DECAY_FACTOR        0.99998 /* decay time constant of 1.0 sec */
#define DROP_LEVEL          0.001  /* -60 dBFS */
#define PI                  3.14159265358979323846

/* commands */
enum {
    CMD_ADD_KEY = 1,
    CMD_RM_KEY
};

/* for each tone */
typedef struct {
    int key; /* keyboard key */  
    double f0; /* frequency associated with key */ 
    double phase_inc; /* phase increment per sample to realize freq */
    double phase; /* save phase value for next sample */
    double attack_factor;
    double decay_factor;
    double attack_amp; /* save attack amplitude for next sample */
    double decay_amp; /* save decay amplitude for next sample */
} Tone;

typedef struct {
#ifdef __APPLE__ 
    atomic_int cmd; /* command from user interface thread */
#else
    int cmd;
#endif
    int new_key;    //key pressed
    double new_freq;//freq associated with key
    int num_keys;   //number of keys voiced
    int num_chan;   //number of channels
    int samp_rate;  //sampling rate of output
    Tone tone[KEYS_VOICED];
} Synth;

    /* function prototypes */
    void init_synth(Synth *ps, int in_num_chan, int in_samp_rate);
    float key2freq(char c);
    void execute_cmd(Synth *ps, int cmd);
    void synth_block(Synth *ps, int len, float *output);
    void add_key(Synth *ps, int new_key, double new_freq);
    void rm_key(Synth *ps);
    void shift_keys(Synth *p);
    void init_key(Synth *ps, int new_key, double new_freq);

#endif /* _SYNTH_H_ */