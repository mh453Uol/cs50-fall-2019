#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int letterToAlphabetIndex(char letter) {
    int asciiIndex = (int)letter;
    int alphabetIndex = 0;

    if(isupper(letter)) {
        // A = 65, B = 66, C = 67, Z = 90
        // 90 (Z) - 65 = 25
        // 67 (C) - 65 = 2
        alphabetIndex = asciiIndex - 65;
    } else {
        // a = 97, b = 98, c = 99, z = 122
        // 99 (c) - 97 = 2
        // 122 (z) - 97 = 25
        alphabetIndex = asciiIndex - 97;
    }

    return alphabetIndex;
}

// Key must be 26 chars length, all alphabets,
// and containing each letter from the alphabet
// exactly once
bool isValidKey(string key, int keyLength) {
    // hashmap where the letter index is the key
    // i.e A = 0, B = 1, C = 2, ... , Z = 25
    bool containsAlphabet[26] = { false };
    int alphabetLetterIndex = 0;

    if(keyLength != 26) {
        return false;
    }

    for(int i = 0; i < 26; i++) {
        if(!isalpha(key[i])) {
            return false;
        }

        alphabetLetterIndex = letterToAlphabetIndex(key[i]);

        if(containsAlphabet[alphabetLetterIndex] == true) {
            return false;
        }

        containsAlphabet[alphabetLetterIndex] = true;

        //printf("%d |",containsAlphabet[i]);
    }
    return true;
}

int main(int argC, char *argV[]) {

    if(argC != 2) {
        printf("Usage: ./substitution key");
        return 1;
    }

    string key = argV[1];
    int keyLength = strlen(key);

    if(!isValidKey(key, keyLength)) {
        printf("Key must contain 26 characters.");
        return 1;
    }

    string plainText = get_string("plaintext:");
    int plainTextLength = strlen(plainText);

    //printf("plain text %s | length: %d",plainText, plainTextLength);

    int plainTextLetterIndex = 0;

    char cipherText[plainTextLength + 1];
    char currentPlainTextLetter = 'a';

    for(int i = 0; i < plainTextLength; i++) {
        //printf("current Index: %d", i);
        currentPlainTextLetter = plainText[i];

        if(isalpha(currentPlainTextLetter)) {
            plainTextLetterIndex = letterToAlphabetIndex(currentPlainTextLetter);

            cipherText[i] = key[plainTextLetterIndex];

            if(isupper(currentPlainTextLetter)) {
                cipherText[i] = toupper(cipherText[i]);
            } else {
                cipherText[i] = tolower(cipherText[i]);
            }
        } else {
            cipherText[i] = currentPlainTextLetter;
        }
    }

    cipherText[plainTextLength] = '\0';

    printf("ciphertext: %s",cipherText);
    printf("\n");
    return 0;
}



