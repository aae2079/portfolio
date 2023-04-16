#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

#define DUR 10
#define FS 48000


int main(int argc, char* argv[]){

	float max_amplitude;
	char *ifile, *ofile;

	// Check's command line arguments. Returns Usage if not correct
	if(argc !=4 ){
		fprintf(stderr, "Usage: %s max_amplitude input_file output_file\n", argv[0]);
		return -1;
	}

	// get max amplitude 
	max_amplitude = atof(argv[1]);

	// get file name
	ifile = argv[2];

	// output file we write to
	ofile = argv[3];

	// open file
	FILE *ifp = fopen(ifile,"r");
	if (ifp == NULL){
		fprintf(stderr, "ERROR: Cannot open %s\n", ifile);
        return -1;
	}

	// read the wav file header
	unsigned char header[44];

    if ( fread(header, sizeof(header), 1, ifp)==0) {
          fprintf(stderr, "Error");
    }

    // print the header values
    for (int i = 0; i < 44; i += 11) {
    	for (int j = i; j < i + 11; j++) {
        	char c = isprint(header[j]) ? header[j] : ' ';
        	printf("%c %02x ", c, header[j]);
    }
    printf("\n");
}


    // checks to see if it is a WAV file
    if (header[0] != 'R' || header[1] != 'I' || header[2] != 'F' || 
    	header[3] != 'F' || header[8] != 'W' || header[9] != 'A' || 
    	header[10] != 'V' || header[11] != 'E' || header[12] != 'f' || 
    	header[13] != 'm' || header[14] != 't' || header[15] != ' ') {
    	fprintf(stderr, "Error: File is not valid\n");
	}

    // Finds value of WAV file info using bit shifting
    int num_channels = header[22] | header[23]<<8;
    printf("Number of channels: %d\n", num_channels);
    int sample_rate = header [24] | header [25]<<8 | header[26]<<16 | header [27] <<24; 
    printf("Sample_rate: %d\n", sample_rate);
    int bits_per_samples = header [34] | header[35]<<8; 
    printf("Bits per samples: %d\n", bits_per_samples);
    int data_size = header[36]| header[37]<<8 | header[38]<<16 | header[39]<<24;
    printf("Size of Data: %d\n", data_size);
    int num_samples = data_size / (num_channels * bits_per_samples/8);
    printf("Number of samples: %d\n", num_samples);


    // Binary calculatons
    short x[DUR*FS]; // length of audio in samples
    int num_samp = DUR*FS; // number of smaples

    // reads the file
    int count1 = fread(x, sizeof(x[0]), num_samp, ifp);
    if ( count1 != num_samp ) {
        fprintf(stderr, "Cannot read wav info\n");
    }

    // calculated max
    int max_x = 0;
    for (int i=0; i<num_samp; i++) {
    	if (abs(x[i]) > max_x) {
    		max_x = abs(x[i]);
          }
    }
    printf("Max Absolute Value: %d\n",max_x);

    // Sets max amplitude from command line to new x array
    for (int i=0; i<num_samp; i++) {
    	x[i] = round( x[i] * ((float)max_amplitude/(float)max_x) );
	}
	
	// opens the output file
	FILE *ofp = fopen(ofile,"w");
	if (ofp == NULL){
		fprintf(stderr, "ERROR: Cannot open %s\n", ofile);
        return -1;
	}

	// write the header and new signal to output file
	fwrite(header, sizeof(header), 1, ofp);
	fwrite(x, sizeof(short), num_samples, ofp);

	fclose(ifp); // close input file
	fclose(ofp); // close output file

	return(0);
    	
}