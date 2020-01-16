def main():
    # 0, 2, 4, 6
    nums = [x for x in range(0,8,2)]
    print(nums)

    nums = list()
    print(nums)

    nums.append(1)
    # 1
    print(nums)

    nums.insert(2,6)
    # 1, 6
    print(nums)

    ##### Tuples #####
    # ordered, immutable set of data

    presidents = [
        ("George", 1789),
        ("John", 1797),
        ("Thomas", 1801),
        ("James", 1809)
    ]

    print(presidents)

    for president, year in presidents:
        print("President: {0}, {1} take office".format(president, year))

    ##### Dictionaries #####

    menu = {
        "margereta": 15.99,
        "vegetable": 12.99
    }

    print(menu)

    if menu["margereta"] == 15.99:
        print("Margereta is expensize")

    print("--Menu--")

    for key in menu:
        print(key)

    # items() convert to list
    for pizza, price in menu.items():
        print(f"{pizza} is £{price}");


if __name__ == "__main__":
    main()