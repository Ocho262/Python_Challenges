import math
import sys

inp = ""
while inp != "1" and inp != "2":
    inp = input("Enter 1 or 2: ")
    if inp != "1" and inp != "2":
        print("You must type 1 or 2")

# Challenge 1: Make sure input is an integer
try:
	length = int(input("What is the length? "))
except:
    print("Value must be an integer.")
    sys.exit(1)

# Challenge 1: Make sure input is an integer
# Challenge 100: Redo as a while loop
try:
    width = int(input("What is the width? "))
except:
	print("Value must be an integer.")
	sys.exit(1)   


	
# challenge 2 note:
# Area (circle)=3.14159r^2
# and show a menu of shapes
# and do a rectangle function and a circle function

if inp == "1":
    def rectangle(length, width):
        area_of_ceiling = float(length * width)
    # Constraint 1: USE A CONSTANT to hold the Conversion Rate
        PAINT_NEEDED = area_of_ceiling / 350
    # Constraint 2: Ensure that you round up to the next whole number
        paint_rounded = math.ceil(PAINT_NEEDED)

if inp == "2":
    def circle(radius):
        area_of_ceiling = float(3.14159 * radius^2)
    # Constraint 1: USE A CONSTANT to hold the Conversion Rate
        PAINT_NEEDED = area_of_ceiling / 350
    # Constraint 2: Ensure that you round up to the next whole number
        paint_rounded = math.ceil(PAINT_NEEDED)

# Fundamental Step: Make the basic program work
# if paint_rounded == 0:
#	paint_rounded = 1

print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded, area_of_ceiling))
