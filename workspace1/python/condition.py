import cs50

x = cs50.get_int("x : ")
y = cs50.get_int("y: ")

# here is a comment
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")