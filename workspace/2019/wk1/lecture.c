#include <stdio.h>
#include <cs50.h>

// compile: clang lecture.c
// a.out

// get_string() is part of cs50.h lib
// to compile we have to link the our code
// with the libary doing clang lecture.c -lcs50

// Make: build tool run using make hello

int main(void) {
    char name[20];
    // scanf not buffer safe i.e user enters move than
    // 20 chars and we try to store in array
    // causes a index out of bounds

    //scanf("%s", name);
    //fgets(name, 20, stdin);

    do {

    int a = get_int("Length: ");
    //printf("Hello %s! \n", name);




    for(int i = 0; i <= a; i++) {
        printf("?");
    }
    printf("\n");

    //pipes i.e
    //xx
    //xx
    //xx
    //xx
    for(int i=0; i < 10;i++) {
        printf("##\n");
    }
    printf("\n");

    }
    while(get_string("contine ? Y/N") == "y" || get_string("contine ? Y/N") == "Y");
}