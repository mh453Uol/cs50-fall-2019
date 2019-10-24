#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // r = read
    // w = write (overwrites existing file)
    // a = append (append to existing file)
    FILE* filePointer = fopen("sample.txt", "r");
    FILE* writeFilePointer = fopen("duplicate.txt","w");

    // pointer is null then file doesnt exists
    if(filePointer == NULL) {
        printf("main:: could not open %s","sample.txt");
        return 1;
    }

    if(filePointer == NULL) {
        printf("main:: could not write %s","duplicate.txt");
        return 1;
    }

    // read next charectar one at a time
    // char currentCharectar = fgetc(filePointer);
    char currentCharectar;

    // while we havent reached end on of file print each charectar
    while((currentCharectar = fgetc(filePointer)) != EOF) {
        printf("%c",currentCharectar);

        // write charectar to file where file must
        // be append or write
        fputc(currentCharectar,writeFilePointer);
    }

    printf("\n-----------------------------\n");

    // Go to beginning of file
    fseek(filePointer, 0, SEEK_SET);

    char words[27];

    // read 1 bytes x 27 so 27 bytes of words
    // and store in buffer words
    fread(words,sizeof(char),27,filePointer);


    for(int i = 0; i < 27; i++) {
        printf("%c",words[i]);
    }

    char numbers[10] = {'1','2','3','4','5','6','7','8','1','0'};
    // write 1 bytes x 10 of data to write file pointer
    fwrite(numbers,sizeof(char), 10, writeFilePointer);

    char c; // char is not pointer
    fread(&c,sizeof(char),1,filePointer);


    fclose(filePointer);
    fclose(writeFilePointer);
}
