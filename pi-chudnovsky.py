# imports
from time import sleep
from decimal import Decimal, getcontext

# set variables
M = Decimal(1)
L = Decimal(13591409)
X = Decimal(1)
K = Decimal(6)
S = L

# main
print("Infinite Calculations: The π Calculator\nMethod: Chudnovsky Algorithm\n")
sleep(1)
digits = int(input("How many digits would you like to calculate? "))
getcontext().prec = digits + 4
for i in range(1, digits):
    M = (K**3 - 16 * K) * M / (i**3)
    L += 545140134
    X *= -262537412640768000
    S += M * L / X
    K += 12
pi = Decimal(426880) * Decimal(10005).sqrt() / S
print("π: " + str(pi)[:digits + 2])