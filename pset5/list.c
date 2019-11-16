#include<stdio.h>
#include<stdlib.h>

int main(void) {
    // allocate consecutive space for 3 ints
    // malloc returns first memory address

    int* list = malloc(3 * sizeof(int));

    // if we have space else malloc returns NULL
    if(list == NULL) {
        return 1;
    }

    list[0] = 1; //*list = 1;
    list[1] = 2; //*(list+1) = 2;
    list[2] = 3; //*(list+2) = 3;

    // realloc used to realloc array content to new space in memory
    // does what happens below
    int* tmp = realloc(list,4 * sizeof(int));

    if(tmp == NULL) {
        return 1;
    }

    tmp[3] = -1;

    // Manually handling reallocation without using
    // realloc
    /*
    int* tmp = malloc(4 * sizeof(int));

    if(tmp == NULL) {
        return 1;
    }

    for(int i = 0; i < 3; i++) {
        //tmp[i] = list[i];
        *(tmp+i) = *(list+i);
        printf("%d %p\n",list[i],&list[i]);
    }

    tmp[3] = -1;
    // free up memory for list
    free(list);
    */

    // list points to first address of tmp
    list = tmp;

    printf("\n");

    for(int j = 0; j < 4; j++) {
        printf("%d %p\n",list[j],&list[j]);
    }

}