#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

int main(int argc, string argv[]) {
    //argc when we run we do ./caesar 1 so ./{caesar} {1} argc = 2
    if(argc != 2) {
        printf("Usage: ./caesar key");
        // return error
        return 1;
    }

    int key = atoi(argv[1]);
    printf("Key: %d", key);

    string plaintext = get_string("plaintext:\t");
    int plainTextLength = strlen(plaintext);

    char cipherText[plainTextLength];
    int rotations = key % 26;
    int asciiIndex = 0;

    for(int i = 0; i < plainTextLength; i++) {
        if(isalpha(plaintext[i])) {
            asciiIndex = (int) plaintext[i] + rotations;

            if(isupper(plaintext[i]) && asciiIndex > 90) {
                asciiIndex = asciiIndex - 26;
            }

            if(islower(plaintext[i]) && asciiIndex > 122) {
                asciiIndex = asciiIndex - 26;
            }

            cipherText[i] = (char) asciiIndex;
        } else {
            cipherText[i] = plaintext[i];
        }
    }
    printf("ciphertext: %s\n", cipherText);
    return 0;
}