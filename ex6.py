x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
"""Below we have a variable assignment with a string_formatter"""
y = "Those who know %s and those who %s" % (binary, do_not)

print(x)
print(y)

# We are formatting the x and y variables.
print("I said: %r " % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# In this we add the formatted variable later then initialization.
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with right side."

# Appending 2 variables.
print(w + e)
