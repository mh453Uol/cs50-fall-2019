#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int value;
    struct node *next;
} node;

void insert(node** head, int value) {
    printf("node: %p\n",&(*head));

    node* currentNode = *head;
    node* node = malloc(sizeof(node));

    node->value = value;
    node->next = NULL;

    // Inserting first node in linked list
    if(*head == NULL) {
         *head = node;
    } else {
        // get last node and link
        currentNode = *head;

    }
}

int main(void) {
    int* length = malloc(sizeof(int));
    *length = 10;

    node* head = NULL;

    printf("main: head: %p\n",&head);
    printf("value: %p\n",&length);

    insert(&head,1);

    insert(&head,2);
    printf("main: value: %d\n",*length);
    //insert(head,tail,3);
    //insert(head,tail,4);
}