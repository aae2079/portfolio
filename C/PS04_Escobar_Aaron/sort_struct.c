#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sort.h"

int read_students(FILE *ifp, struct Student *sdata){
    char line[LINE_LEN];
    char *token = NULL;
    int i = 0;
    while(fgets(line,LINE_LEN,ifp)){
    	token = strtok(line, ",\n");
    	strcpy(sdata[i].last, token);
        token = strtok(NULL, ",\n");
        strcpy(sdata[i].first, token);
        token = strtok(NULL, ",\n");
        sdata[i].id = atoi(token);
        i++;
    }
    return i;

    for (int i = 0; i < MAX_STUDENTS; i++) {
        if (fgets(line, LINE_LEN, ifp) == NULL) {
            break;
        }    
    }
    return 0;
}

int sort_students(char *sort_key, int num_students, struct Student *sdata) {
    if (strcmp(sort_key, "last") == 0) {
        qsort(sdata, num_students, sizeof(struct Student), comp_last);
    } else if (strcmp(sort_key, "first") == 0) {
        qsort(sdata, num_students, sizeof(struct Student), comp_first);
    } else if (strcmp(sort_key, "id") == 0) {
        qsort(sdata, num_students, sizeof(struct Student), comp_id);
    } else {
        return 1;
    }

    return 0;
}


int comp_last(const void * a, const void * b){
	struct Student *pa = (struct Student *)a;
    struct Student *pb = (struct Student *)b;

    return(strcmp(pa->last, pb->last));
}
int comp_first(const void * a, const void * b){
	struct Student *pa = (struct Student *)a;
    struct Student *pb = (struct Student *)b;

    return(strcmp(pa->first, pb->first));
}
int comp_id(const void * a, const void * b){
	struct Student *pa = (struct Student *)a;
    struct Student *pb = (struct Student *)b;

    return pa->id - pb->id;
}
void write_students(FILE *ofp, int num_students, struct Student *sdata){
	for (int i = 0; i < num_students; i++) {
		fprintf(ofp, "%s,%s,%d\n", sdata[i].last,sdata[i].first,sdata[i].id);
    }
  
}