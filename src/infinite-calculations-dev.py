# imports
from time import sleep

# configure print() to always forcibly flush
orig_print = print
def print(string: str):
    orig_print(string, end = "", flush = True)

# main
print("Welcome to Infinite Calculations\nVersion: 0.2.0-beta\nCopyright 2024 Te Du\n\n")
sleep(1)
print("What would you like to calculate?\n(A) π: Chudnovsky Algorithm\n(B) π: Gosper's series\n(C) √2\n(D) Fibonacci Sequence\n\n")
sleep(1)
try:
    calculation_option = input("Type A, B, C or D: ").lower()
    print("\n")
    if calculation_option == "a":
        # π: Chudnovsky Algorithm

        # imports
        from decimal import Decimal, getcontext

        # set variables
        M = Decimal(1)
        L = Decimal(13591409)
        X = Decimal(1)
        K = Decimal(6)
        S = L

        # main
        print("Infinite Calculations: The π Calculator\nMethod: Chudnovsky Algorithm\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        getcontext().prec = digits + 4
        for i in range(1, digits):
            M = (K**3 - 16 * K) * M / (i**3)
            L += 545140134
            X *= -262537412640768000
            S += M * L / X
            K += 12
        pi = Decimal(426880) * Decimal(10005).sqrt() / S
        print("\nπ: " + str(pi)[:digits + 2])
    elif calculation_option == "b":
        # π: Gosper's series

        # set variables
        Q = 60
        R = 13440
        T = 10080
        I = 3

        # main
        print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        print("\n\nπ: 3.")
        for i in range(digits):
            digit = ((I * 27 - 12) * Q + R * 5) // (T * 5)
            print(digit)
            U = I * 3
            U = (U + 1) * 3 * (U + 2)
            R = U * 10 * (Q * (I * 5 - 2) + R - T * digit)
            Q *= 10 * I * (I * 2 - 1)
            I += 1
            T *= U
    elif calculation_option == "c":
        # √2

        # imports
        from decimal import Decimal, getcontext

        # main
        print("Infinite Calculations: The √2 Calculator\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        getcontext().prec = digits + 4
        print("\n√2: " + str(Decimal(2).sqrt())[:digits + 2])
    elif calculation_option == "d":
        # Fibonacci Sequence

        # set variables
        fib = [0, 1]

        # main
        print("Infinite Calculations: The Fibonacci Calculator\n\n")
        sleep(1)
        digits = int(input("How many terms would you like to calculate? "))
        if digits < 1:
            raise ValueError
        print("\nFibonacci Sequence: 0")
        if digits > 1:
                print(", 1")
        if digits > 2:
            for i in range(digits - 2):
                if i != digits - 2:
                    print(", ")
                fib.append(fib[0] + fib[1])
                print(fib[-1])
                del fib[0]
    else:
        raise ValueError
except ValueError:
    print("\nERROR: Invalid value.")
except MemoryError:
    print("\nERROR: Not enough memory to complete process.")
except:
    print("\nERROR: Unknown error.")
sleep(1)
input("\n\nPress Enter to exit...")