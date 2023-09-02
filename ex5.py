name = "Zed A. Shaw"
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"
statement = "print this no matter what"

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy.k" % weight)
print("Actually he's not too heavy.")
print("He's got %s eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)
print("This what I wanted to print %r" % statement)

# this line is tricky, try to get it exactly right
print(
    "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
)
