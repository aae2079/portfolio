#include <stdio.h>
#include <string.h>

int my_atoi(char *s) {
     int n = 0;
     int len = strlen(s);
     for(int i=0; i < len; i++){
          int value = s[i] - '0';
          n = n*10 + value;
     }

     return n; 
}
int main() {
     char *s1 = "153";
     char *s2 = "23";
     printf("The sum of %s and %s is %i\n", s1, s2,
          my_atoi(s1) + my_atoi(s2));
     return 0;
}