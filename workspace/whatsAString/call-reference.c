#include<stdlib.h>
#include<stdio.h>

void increment(int* a) {
    *a = (*a)+1;
    printf("increment:: Address of a = %p \n",&a);
}
int main(void) {
    int a = 10;
    increment(&a);
    printf("main:: Address of a = %p \n",&a);
    printf("main:: a = %d",a);
}

