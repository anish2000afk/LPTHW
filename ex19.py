# Simple function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


# Calling the function with numbers are args.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# We create new variables from our scripts and assign them.
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We can use math arguements
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Combining previous variables with math for arguements.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

'''10 different ways to call a function
    Generally speaking we can use any variable asssingnment as a function.
1. Function inside a function
2. Boolean value as a function
3. Taking input values from user as a function.
4. Using argv as a function arguement.
5. Taking a file as a function ( like a variable with .read)???
6. Taking len as a parameter.
7.  Do it later'''
