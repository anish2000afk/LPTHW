# imports argv from the sys module
from sys import argv

# we assign 2 variables to argv.
script, filename = argv

# use open function and assign the file to txt variable
txt = open(filename)

# We print the file name
print("Here's your file %r:" % filename)
# We use the read function on txt to print out the contents of the file.
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
