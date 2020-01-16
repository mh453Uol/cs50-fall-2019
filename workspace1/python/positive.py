import cs50

def main():
    i = get_positive_int("Positive integer: ")
    print(i)

def get_positive_int(message):
    userInput = -1;
    while userInput <= 0:
        userInput = cs50.get_int(message)
    return userInput

if __name__ == "__main__":
    main()