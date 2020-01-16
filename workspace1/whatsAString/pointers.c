#include<stdlib.h>
#include<stdio.h>

int main(void) {
    // Under the hood a string is a pointer to the first char in the word
    // we keep reading until \0 (null terminator)
    char *s = "EMMA";
    printf("%p\n",s);
    // Should be same as above printf
    printf("%p\n",&s[0]);
    printf("--------------------------\n");
    int a;
    int *p; // pointer
    a = 10;
    p = &a; // &a = address of a
    printf("%p\n",p); // memory address
    printf("%d\n",*p); // *p = value at address pointed by p
    printf("%p\n",&a); // memory address of a

    printf("a = %d\n",*p);
    *p = 90; // deferencing
    printf("a = %d\n",*p);

    printf("--------------------------\n");
    int c = 900;
    *p = c; // value at memory address p is c
            // so a is 900;

    printf("a = %d\n",a);
    printf("a ~ %p\n",&a);
    printf("p = %p\n",p);

    printf("--------------------------\n");
    int j = 10;
    int* i = &a;
    // Pointer arithmetic
    printf("Address p is %p\n",i); // p is 2002
    printf("Size of integer is %ld bytes\n",sizeof(int));
    printf("Address p+1 is %p\n",i+1);
    printf("Value at p+1 is %d\n",*i+1);

    printf("--------------------------\n");
    // why pointers are strong types
    int y = 1025;
    int* z = &y;
    printf("Size of integer is %ld bytes\n",sizeof(int));
    printf("Address = %p, value = %d\n",z,*z);

    char* a1 = (char*)z; //typecasting
    // int is 4 bytes | char is 1 byte
    // so we lose {00000000 0000000 0000000} 0000000
    // bits in {}

    printf("size of char is % ld bytes\n",sizeof(char));
    printf("Address = %p, value = %d\n",a1,*a1); // 1025 = 00000000 00000000 00000100 {0000001} = 1
    printf("Address = %p, value = %d\n",(a1+1),*(a1+1)); // 1025 = 00000000 00000000 {00000100} 0000001 = 4



}