from cs50 import get_int

numbers = [];

def main():
    while True:
        input = get_int("Number: ")
        numbers.append(input)

def log():
    for n in numbers:
        print(n)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print()
        log()
