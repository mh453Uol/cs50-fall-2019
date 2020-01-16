import cs50
s = cs50.get_string("Name: ")

for c in s:
    c.upper()
    print(c, end="");