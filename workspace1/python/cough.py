import cs50

x = cs50.get_int("range: ")
# own main function
def main():
    cough(x)

def cough(x):
    for i in range(x):
        print("cough")

main()

