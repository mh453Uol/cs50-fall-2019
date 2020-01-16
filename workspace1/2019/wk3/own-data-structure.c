#include<cs50.h>
#include<stdio.h>

typedef struct {
    string name;
    int age;
} Person;

int main(void) {

    Person people[2];

    people[0].name = "Majid";
    people[0].age = 23;

    people[1].name = "Zain";
    people[1].age = 1;

    printf("|\t Name \t|\t Age \t|");

    for(int i = 0; i < 2; i++) {
     printf("\n|\t %s \t|\t %d \t|", people[i].name, people[i].age);
    }

    printf("Hello World");
}