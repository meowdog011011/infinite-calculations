# imports
from time import sleep
from decimal import Decimal, getcontext

# set variables
x_n = Decimal(1)

# main
print("Infinite Calculations: The √2 Calculator\nMethod: Newton's algorithm\n")
sleep(1)
digits = int(input("How many digits would you like to calculate? "))
getcontext().prec = digits + 4
precision = Decimal(1) / int(eval("1e+" + str(digits + 1)))
while True:
    x_next = (x_n + 2 / x_n) / 2
    if abs(x_next - x_n) < precision:
        break
    x_n = x_next
print("√2: " + str(x_next)[:digits + 2])