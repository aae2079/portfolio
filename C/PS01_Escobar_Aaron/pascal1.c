#include <stdio.h>

int main(){
	
	int n;
	printf("Enter the number of rows: ");
    scanf("%d", &n);

    int pascal[n][n];

	for(int i = 0; i < n; i++){
		for (int j = 0; j <=i; j++){
			if (j == 0 || j == i){
				pascal[i][j] = 1;
			}
			else{
				pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
			}
			printf("%5d", pascal[i][j]);
		}
		printf("\n");
	}

	
	return 0;
}