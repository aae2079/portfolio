#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){

	float x1,x2, y;
	char operator;

	if(argc !=4 ){
		printf("Usage: ./clc x1 operator x2 where x1, x2 are floats and operators are + - x / \n");
		return 1;
	}
	
	x1  = atof(argv[1]);
	x2 = atof(argv[3]);
	
	operator = argv[2][0];

	switch(operator){
		case '+':
			y = x1+x2;
			break;
		case '-':
			y = x1-x2;
			break;
		case 'x':
			y = x1*x2;
			break;
		case '/':
			if (x2 ==0){
				printf("Error: divide by 0 \n");
				return 1;
			}
			y = x1/x2;
			break;
		default:
			 printf("Error: invalid operator '%c'\n", operator);
			 return 1;
        }
    printf("%f %c %f is %f\n", x1, operator, x2, y);
	
	return 0;
}