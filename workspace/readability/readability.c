#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

int getLetterCount(string text) {
    int count = 0;
    int length = strlen(text);

    for(int i = 0; i < length; i ++) {
        if(isalpha(text[i])) {
            count++;
        }
    }

    return count;
}

int getWordCount(string text) {
    // typically end of sentence i.e majid is the best| {best} doesnt have a space
    // so we start from 1
    int count = 1;
    int length = strlen(text);

    for(int i = 0; i < length; i++) {
        if(text[i] == ' ') {
            count++;
        }
    }
    return count;
}


int getSentenceCount(string text) {
    int count = 0;
    int length = strlen(text);

    for(int i = 0; i < length; i++) {
        if(text[i] == '.' || text[i] == '!' || text[i] == '?') {
            count++;
        }
    }
    return count;
}

int textDifficulty(float letterCount, float wordCount, float sentenceCount) {
    // use Coleman-Liau formula to compute text grade difficulty
    // index = 0.0588 * L - 0.296 * S - 15.8
    // L = average number of letters per 100 words in the text
    // S = average number of sentences per 100 words in the text
    //printf("Letter Count: %f \t", letterCount);
    //printf("Word Count: %f \t", wordCount);
    //printf("Sentence Count: %f \t", sentenceCount);

    //printf("---- (letterCount / wordCount) %f \t", ((letterCount / wordCount)));
    //printf("---- (sentenceCount / wordCount) %f \t", ((sentenceCount / wordCount)));

    float index = 0.0588 * ((letterCount / wordCount) * 100) - 0.296 *
        ((sentenceCount / wordCount) * 100) - 15.8;

    int rounded = roundf(index);

    return rounded;
}

int main(void) {
    string text = get_string("Text: ");

    int letterCount = getLetterCount(text);
    //printf("%d, letter(s) \n", letterCount);

    int wordCount = getWordCount(text);
    //printf("%d word(s) \n", wordCount);

    int sentenceCount = getSentenceCount(text);
    //printf("%d sentence(s) \n", sentenceCount);

    int index = textDifficulty((float)letterCount, (float)wordCount, (float)sentenceCount);
    //printf("index: %d", index);

    if(index >= 16) {
        printf("Grade 16+\n");
    } else if(index > 1) {
        printf("Grade %d\n", index);
    } else {
        printf("Before Grade 1\n");
    }

    return 0;
}