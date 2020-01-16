#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, char *argv[])
{

    int px = 104;

    int* px2 = malloc(4);
    *px2 = 24;

    int* px3 = malloc(sizeof(int));
    *px3 = 25;

    printf("malloc px2 address %p, value %d\n",px2,*px2);
    printf("malloc px3 address %p, value %d\n",px3,*px3);
    printf("stack px address %p, value %d\n",&px,px);

    int x = get_int("Enter boxes: \n");

    // array on the heap
    int* heap_array = malloc(x * sizeof(float));

    for(int i = 0; i < 10; i++) {
        heap_array[i] = 10;
    }

    for(int i = 0; i < 10; i++) {
        printf("%d, ",heap_array[i]);
    }

    // free dynamically create memory
    free(px2);
    free(px3);
    free(heap_array);



}