"""This prog converts inches and pounds to centimeters and kilos """
height_inches = float(input())
weight_pounds = float(input())

height_centimeters = height_inches * 2.54
weight_kilos = weight_pounds / 2.205

print("Your height in inches is %s" % height_inches)
print("Your height in centimeters is %s" % height_centimeters)
print("Your weight in pounds is %s" % weight_pounds)
print("Your weight in kilos is %s" % weight_kilos)
