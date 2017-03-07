import math

length = input("What is the length?")
width = input("What is the width? ")

CONST_PAINT = 350

try:
   val = int(length)
   val = int(width)
except ValueError:
   print("That's not an int!")

area_of_ceiling = length * width
paint_needed = area_of_ceiling / CONST_PAINT
paint_rounded = math.ceil(paint_needed)

print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded, area_of_ceiling))
