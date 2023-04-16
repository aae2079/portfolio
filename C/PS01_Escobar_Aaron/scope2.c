#include <stdio.h>

int i;

int main(){
  for (int i = 1; i <= 10; i++){
  printf("%d\n",i);
}
printf("%d\n",i);
}

/* 

a. It prints out 0. 

b. In this case the int i outside of the main function is 
outside the scope of the loop thus it becomes a throw away variable which is why 
it outputs 0

*/