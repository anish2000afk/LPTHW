from sys import argv

script, filename = argv

print("We are going to erase %r" % filename)
print("If you don't want that, then hit ...")
print("If yo do want that press ENTER")

input("?")

print("Opening the file")
target = open(filename, "w")

print("Truncating the file. Goodbye!!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file")

# Modded line
lines = "%s\n%s\n%s" % (line1, line2, line3)
target.write(lines)

print("And finally we close it.")
target.close()
