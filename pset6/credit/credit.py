from cs50 import get_int, get_string
import math


def main():
    while True:
        textualCardNumber = get_string("Number: ")

        if textualCardNumber.isdigit():
            cardNumber = int(textualCardNumber)
            issurer = getCardIssuer(cardNumber)

            if issurer == "INVALID":
                print("INVALID")
                break
            else:
                # Valid card number using Luhn
                if luhnChecksum(textualCardNumber):
                    print(issurer)
                    break
                else:
                    print("INVALID")
                    break


def luhnChecksum(textualCardNumber):
    evenIndexedNumbersTotal = 0
    oddIndexedNumbersTotal = 0
    currentNumber = 0
    currentIndex = len(textualCardNumber) - 1
    isEven = False

    while currentIndex >= 0:
        currentNumber = int(textualCardNumber[currentIndex])
        if (isEven):
            evenIndexNumber = currentNumber * 2
            if evenIndexNumber >= 10:
                # 19 so we want 1 + 9 product digits
                evenIndexedNumbersTotal += 1 + (evenIndexNumber % 10)
            else:
                evenIndexedNumbersTotal += evenIndexNumber

            isEven = False
        else:
            oddIndexedNumbersTotal += currentNumber
            isEven = True

        currentIndex = currentIndex - 1

    return ((evenIndexedNumbersTotal + oddIndexedNumbersTotal) % 10) == 0


def getCardIssuer(cardNumber):
    # 1. Check its valid American Express, MasterCard, Visa
    americanExpress = isAmericanExpress(cardNumber)
    masterCard = isMasterCard(cardNumber)
    visa = isVisa(cardNumber)

    if americanExpress:
        return "AMEX"
    elif masterCard:
        return "MASTERCARD"
    elif visa:
        return "VISA"
    else:
        return "INVALID"


def isAmericanExpress(cardNumber):
    return ((cardNumber >= 340000000000000 and cardNumber <= 349999999999999) or
            (cardNumber >= 370000000000000 and cardNumber <= 379999999999999))


def isMasterCard(cardNumber):
    return ((cardNumber >= 5100000000000000 and cardNumber <= 5199999999999999) or
            (cardNumber >= 5200000000000000 and cardNumber <= 5299999999999999) or
            (cardNumber >= 5300000000000000 and cardNumber <= 5399999999999999) or
            (cardNumber >= 5400000000000000 and cardNumber <= 5499999999999999) or
            (cardNumber >= 5500000000000000 and cardNumber <= 5599999999999999))


def isVisa(cardNumber):
    return ((cardNumber >= 4000000000000 and cardNumber <= 4999999999999) or
            (cardNumber >= 4000000000000000 and cardNumber <= 4999999999999999))


main()
