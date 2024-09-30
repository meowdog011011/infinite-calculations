# imports
from time import sleep
from functools import partial

# configure print() to always forcibly flush
print = partial(print, flush = True)

# set variables
fib = [0, 1]

# main
print("Infinite Calculations: The Fibonacci Calculator\n")
sleep(1)
digits = int(input("How many digits of the Fibonacci sequence would you like to calculate? "))
if digits < 3:
    print("Output: ", end = "")
    for i in range(digits):
        sleep(0.1)
        print(fib[i], end = "")
        if i != digits - 1:
            print(", ", end = "")
else:
    print("Output: 0, 1, ", end = "")
    for i in range(digits - 2):
        sleep(0.1)
        fib.append(fib[0] + fib[1])
        print(fib[-1], end = "")
        if i != digits - 3:
            print(", ", end = "")
        del fib[0]