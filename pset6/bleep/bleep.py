from cs50 import get_string
from sys import argv


def main():
    # 1. Single argument which is path i.e /words/banned.txt,
    #   banned-word.txt etc
    #   1.2 if no args then exit()
    # 2. Read file and store each word into memory,
    #   2.1 File looks like:
    #       darn
    #       drat
    #       fiddlesticks
    #   2.2 So word is on each line (\n)
    # 3. Get user input
    # 4. Tokenize each word i.e split on space since user
    #   input is like 'school sucks'
    # 5. If sucks is a banned word return
    #   school *****

    if len(argv) != 2:
        exit("Usage: python bleep.py dictionary")

    bannedWordsPath = argv[1]
    bannedWords = set()

    with open(bannedWordsPath, "r") as file:
        for line in file:
            # remove \n from end and add to set
            bannedWords.add(line[:-1])

    message = get_string("What message would you like to censor?\n")

    # split message on the space
    tokenized = message.split()

    censoredMessage = ""

    for token in tokenized:
        if token.casefold() in bannedWords:
            # replace token i.e sick with ****
            censoredWord = ""
            for letter in token:
                censoredWord += "*"
            censoredMessage += censoredWord + " "
        else:
            censoredMessage += token + " "

    censoredMessage = censoredMessage[:-1]
    print(censoredMessage)

if __name__ == "__main__":
    main()
