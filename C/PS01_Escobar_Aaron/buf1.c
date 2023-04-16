#include <stdio.h>
#define LEN 100
int i, j;
int main(void) {
    int my_array[LEN];
    j = 0;
    for (i=0; i<LEN+j; i++) {
        my_array[i] = i;
    }
    printf("i is %i\n", i);
return 0; }

/*

a. The terminal outputs "i is 100" after compiling 

