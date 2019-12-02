from cs50 import get_int


def main():

    while True:
        height = get_int("Height: ")

        if height > 0 and height < 9:
            # Height: 4
            #xxx#xx#
            #xx##  ##
            #x###  ###
            #####  ####

            # 4 - 1 = 3 x`s and 3 spaces
            # 4 - 2 = 2 x`s
            # 4 - 3 = 1 x`s
            spaces = height
            blocks = 0
            textualBlocks = ""
            textualSpaces = ""

            for i in range(height):
                spaces = spaces - 1
                blocks = blocks + 1
                textualSpaces = repeatString(" ", spaces)
                textualBlocks = repeatString("#", blocks)
                print(f"{textualSpaces}{textualBlocks}  {textualBlocks}")
            break


def repeatString(string, repeat):
    transformedString = ""

    for i in range(repeat):
        transformedString += string

    return transformedString


main()

