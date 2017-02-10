subtotal = input("What is the order amount? ")
print(subtotal)
subtotal = float(subtotal)

f_subtotal = '{:20,.2f}'.format(subtotal)
f_subtotal = str(f_subtotal)
print("subtotal: " + f_subtotal)
state = raw_input("What is the state? ")
if (state == "MD"):
    print("subtotal: " + f_subtotal)
    taxrate = float(0.06)
    tax = taxrate * subtotal
    tax = float(tax)
    f_tax = ('{:20,.2f}'.format(tax))
    f_tax = str(f_tax)
    print("Sales Tax: " + f_tax)
    total = tax + subtotal
    f_Total = ('{:20,.2f}'.format(total))
    f_Total = str(f_Total)
    print("Total: " + f_Total)
else:
    print("Don't know where that is.")
