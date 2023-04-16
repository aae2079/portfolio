/* FIR filtering of a entire WAV file */

#include <stdio.h>
#include <stdlib.h>			//malloc
#include <string.h>			//memset
#include <sndfile.h>		//sndfile
#include "filter.h"	//declares struct Filt

/* instantiation of FIR filter struct */
struct FIR_Filt filt = {
	/* FIR filter length */
	191,
	/* b coefficients */
	{
#include "fir_filt_coef.h" //FIR filter coefficients
	}
};

int main(int argc, char *argv[])
{
	char *ifile, *ofile;
    SNDFILE *isndfile, *osndfile;
    SF_INFO isfinfo, osfinfo;
    float *ifbuf, *ofbuf;
	int count;

	/* usage and parse command line */
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
    
    ifbuf = (float*)malloc(sizeof(float) * (N-1)*C);
    ofbuf = (float*)malloc(sizeof(float) * (N+M-1) * C);

	/* Read input WAV file into ifbuf */
    
    count = sf_read_float(isndfile,ifbuf,N*C);
    
    if (count != N * C) {
    	printf("Error reading input file %s\n", ifile);
    		exit(-1);
    }

	/* 
	 * filter
	 */
	double *b = filt.b;	//pointer to FIR filter coefficients
	
	for (int n=0; n<N+M-1; n++) {
          for (int k=0; k<M; k++) {
          	ofbuf[n] += ifbuf[n-k+M-1] * b[k];
          } 
	}
	
	count = sf_write_float(osndfile,ofbuf,(N+M-1)*C);
	
	if (count != (N+M-1) * C) {
		printf("Error writing output file %s\n", ofile);
    	exit(-1);
		}


	/* close WAV files 
	 * free allocated storage
	 */

	sf_close(osndfile);
	sf_close(isndfile);

	free(ifbuf);
	free(ofbuf);

	return 0;
}
