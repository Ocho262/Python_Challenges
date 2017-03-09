import math
#def circle():
#	ask "What is the Radius?"
#	PI = 3.14159
#	area_of_ceiling = float(2 * PI * radius^2)

def rectangle():
    numerical = False
    while numerical == False:
        try:
            length = int(input("What is the length? "))
	    numerical = True
	except:
	    print("Input must be an integer. Please try again.")

    numerical = False
    while numerical == False:
         try:
            width = int(input("What is the width? "))
            numerical = True
         except:
            print("Input must be an integer. Please try again.")

    area_of_ceiling = float(length * width)
    PAINT_NEEDED = area_of_ceiling / 350
    paint_rounded = math.ceil(PAINT_NEEDED)

    print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded, area_of_ceiling))

answer = False
choice = raw_input("Circle or Rectangle?")
while answer == False:
	if choice == "circle":
		answer = True
		circle()
	elif choice == "rectangle":
		answer = True
		rectangle()
