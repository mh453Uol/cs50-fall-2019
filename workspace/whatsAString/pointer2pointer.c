#include<stdlib.h>
#include<stdio.h>

int main(void) {
    // | x  | p | q | r |
    // | 10 | x | p | q |
    //

    int x = 5;
    int* p = &x;
    *p = 10;

    int** q = &p;
    int*** r = &q;

    printf("Value of p = %d\n",*p); // 10
    printf("Value of *q = %p\n",*q); //Address of p
    printf("Value of **q = %d\n",*(*q)); //*(205) Value of address 205
    printf("Value of **r = %d\n",***r); //*(210(205))

    ***r = 99;
    printf("Value of x = %d\n",x);
}