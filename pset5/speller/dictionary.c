// Implements a dictionary's functionality
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>

#include "dictionary.h"
//https://speller.cs50.io/cs50/problems/2019/x/challenges/speller#user/mh453Uol
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
// Hash table store at most 180,000 unique hashes however
// can you chaining if we hit hash collisions
const unsigned int N = 180000;

// Hash table
node *table[N] = { NULL };

unsigned int dictionarySize = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int hashedWordArrayIndex = hash(word);
    // hash table key doesnt exist
    if(table[hashedWordArrayIndex] == NULL) {
        return false;
    } else {
        // 0[]
        // 1[] -> {word: 'fred', next -> {word: 'fred ', next -> NULL}}
        // iterate through chains for word
        node *node = table[hashedWordArrayIndex];
        // iterate throught linked list
        while(node != NULL) {
            // if case insensative match return true;
            if(strcasecmp(word,node->word) == 0) {
                return true;
            }
            node = node->next;
        }
        return false;
    }
}

/**
 * A case-insensitive implementation of the djb2 hash function.
 *
 * https://github.com/hathix/cs50-section/blob/master/code/7/sample-hash-functions/good-hash-function.c
 */
 unsigned int hash(const char *word)
{
    unsigned long hash = 5381;

     for (const char* ptr = word; *ptr != '\0'; ptr++)
     {
         hash = ((hash << 5) + hash) + tolower(*ptr);
     }

     return hash % N;
}

void insert(const char *word) {
    // 1. generate hash
    // 2. check hash index exists in hash table
    //      2.1 if so set node as head and reattach old head
    //      2.2 if not add it into the hash table
    int hashedWordArrayIndex = hash(word);

    if(table[hashedWordArrayIndex] == NULL) {
        node *h = malloc(sizeof(node));
        strcpy(h->word, word);
        h->next = NULL;

        table[hashedWordArrayIndex] = h;
    } else {
        // hash collision
        // 0 []
        // 1 []->{word: hello, next: null}
        // Set array index to point new node and attach old node to new node
        // 0 []
        // 1 []->{word: hello2, next -> {word: hello, next: null}}

        // 1. create node n set array to point to new node n
        // 2. node n set next to point to old node
        node *headNode = table[hashedWordArrayIndex];
        node *h = malloc(sizeof(node));
        strcpy(h->word, word);
        h->next = headNode;

        table[hashedWordArrayIndex] = h;
    }
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    //1. Load dictionary file
    //1.1 read each line
    //1.2 convert each word in to a number - hashing
    //1.3 store in data structure

    // open file
    FILE *file = fopen(dictionary, "r");

    if(file == NULL) {
        //printf("dictionary.c :: could not open %s",dictionary);
        return false;
    }

    // {word}{\0 NULL CHARECTAR}
    char word[LENGTH + 1];
    int index = 0;
    int hashedWordArrayIndex = 0;

    for (int c = fgetc(file); c != EOF; c = fgetc(file))
    {
        if(c != '\n') {
            word[index] = c;
            index++;
        } else {
            word[index] = '\0';

            // inserted word in dictionary
            insert(word);
            dictionarySize++;




            //printf("%s\n",table[hashedWordArrayIndex]->word);

            index = 0;
        }
    }

    //printf("dictionary.c :: entries in dictionary %i \n",dictionarySize);
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return dictionarySize;
}

bool unloadLinkedList(node *head) {
    if(head == NULL) {
        return true;
    }
    unloadLinkedList(head->next);
    free(head);
    return true;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // free all malloced memory
    for(int i = 0; i < N; i++) {
        // node created so need to go to end of linked list and free each node
        if(table[i] != NULL) {
            node *node = table[i];
            unloadLinkedList(node);
        }
    }
    return true;
}


