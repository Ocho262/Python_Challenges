import math

length = int(input("What is the length?"))
width = int(input("What is the width? "))

ea_of_ceiling = length * width
paint_needed = area_of_ceiling / const.paint
paint_rounded = math.ceil(paint_needed)


print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded, area_of_ceiling))
