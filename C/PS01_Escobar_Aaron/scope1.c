#include <stdio.h>

int i;

int main(){
  for (i = 1; i <= 10; i++){
  printf("%d\n",i);
}
printf("%d\n",i);
}

/* 

a. It prints out 11

b. The reason is becuase the for loop looks for the integer after 10 which is 11 and then it breaks the loop

*/


