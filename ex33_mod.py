"""This is the modified version of file acc. to Study Drills"""


def list_printer(num, increment):
    i = 0
    numbers = []

    while i < num:
        # Print first iteration of i
        print("At the top i is %d" % i)
        # Then append it to a list.
        numbers.append(i)
        # Auto increment by 1
        i += increment
        print("Numbers now: ", numbers)
        # Prints the final value of i.
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)


"""This is the above code but with for-loop"""


def list_printer_for(num, increment):
    i = 0
    numbers = []

    for i in range(0, num, increment):
        # print first iteration of i
        print("at the top i is %d" % i)
        # then append it to a list.
        numbers.append(i)
        # auto increment by 1
        print("numbers now: ", numbers)
        # prints the final value of i.
        print("at the bottom i is %d" % i)

    print("the numbers: ")

    for num in numbers:
        print(num)


list_printer_for(6, 2)
