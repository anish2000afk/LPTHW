i = 0
numbers = []

while i < 6:
    # Print first iteration of i
    print("At the top i is %d" % i)
    # Then append it to a list.
    numbers.append(i)
    # Auto increment by 1
    i += 1
    print("Numbers now: ", numbers)
    # Prints the final value of i.
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)
