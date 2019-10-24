#include <cs50.h>
#include <stdio.h>

void printSymbol(char symbol, int number, bool newLine) {
    for(int i = 0; i < number; i++) {
        printf("%c",symbol);
    }

    if(newLine) {
        printf("\n");
    }
}

int main(void)
{
    int height = 0;
    do {
        height = get_int("Height: ");
    } while(!(height >=1 && height <= 8));

    // Height: 3
    // **#*#**
    // *##*##*
    // ###*###
    for(int i=1; i<=height; i++){

        // 3 - 1 = 2
        // 3 - 2 = 1
        // 3 - 3 = 0
        int leftBlankSpaces = height - i;
        printSymbol(' ', leftBlankSpaces, false);

        int leftHashes = height - leftBlankSpaces;
        printSymbol('#', leftHashes, false);

        printf(" ");

        printSymbol('#', leftHashes, false);

        printSymbol(' ', leftBlankSpaces, true);
    }
}
