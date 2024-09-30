# imports
from time import sleep
from functools import partial

# configure print() to always forcibly flush
print = partial(print, end = "", flush = True)

# set variables
q = 60
r = 13440
t = 10080
i = 3

# main
print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\nπ: ")
sleep(1)
print("3")
sleep(0.1)
print(".")
while True:
    sleep(0.1)
    digit = ((i * 27 - 12) * q + r * 5) // (t * 5)
    print(digit)
    u = i * 3
    u = (u + 1) * 3 * (u + 2)
    r = u * 10 * (q * (i * 5 - 2) + r - t * digit)
    q *= 10 * i * (i * 2 - 1)
    i += 1
    t *= u