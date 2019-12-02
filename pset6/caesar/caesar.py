from sys import argv
import cs50


def main():
    # 1. get command line argument a hashed password
    # 2. password <= 5 digits
    #   2.1 password alphabetic chars (uppercase and/or lowercase)
    #   2.2 password examples MAjiD
    # 3. hash looks like {50}{GApilQSG3E2}
    #   3.1 50 is salt
    # 4. generate all permutations i.e lowercase, uppercase, mixed
    #   4.1 50GApilQSG3E2 == crypt(aaaaa,50)
    #   4.2 50GApilQSG3E2 == crypt(baaaa,50)
    #   4.3 50GApilQSG3E2 == crypt(zaaaa,50)
    #   4.4 50GApilQSG3E2 == crypt(abaaa,50)

    if len(argv) == 1 or len(argv) > 2:
        print("Usage: ./caesar key")
        exit("Usage: ./caesar key")

    key = int(argv[1])
    plainText = cs50.get_string("plaintext:\n")
    rotations = key % 26
    asciiIndex = 0
    cipherText = ""

    for c in plainText:

        if c.isalpha():
            asciiIndex = ord(c) + rotations

            if c.isupper() and asciiIndex > 90:
                asciiIndex = asciiIndex - 26

            if c.islower() and asciiIndex > 122:
               asciiIndex = asciiIndex - 26

            cipherText += chr(asciiIndex)
        else:
            cipherText += c

    print(f"ciphertext: {cipherText}\n");
    return 0

main()