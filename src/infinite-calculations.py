# imports
from sys import set_int_max_str_digits
from time import sleep, time
from _pydecimal import Decimal, getcontext

# print "Initializing..."
print("Initializing...\n")
sleep(1)

# set unlimited str->int digit conversions
set_int_max_str_digits(0)

# configure print() to always forcibly flush
orig_print = print
def print(string: str):
    orig_print(string, end = "", flush = True)

# define variables
result = "\n"
error = "\n"

# main
print("---------------\n\nWelcome to Infinite Calculations\nVersion: 0.1.0\nWarning: This beta version is not meant for production. May contain bugs.\nCopyright 2024 Te Du\n\n")
sleep(1)
print("What would you like to calculate?\n(A) π / Pi\n(B) √2 / Square root of 2\n(C) e / Euler's number\n(D) φ / Golden Ratio\n\n")
sleep(1)
try:
    calculation_option = input("Type A, B, C or D: ").lower()
    if calculation_option == "a":
        # π: Chudnovsky Algorithm

        # define binary splitting algorithm
        def binary_split(a, b):
            if a + 1 == b:
                Pab = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Qab = 10939058860032000 * a ** 3
                Rab = Pab * (545140134 * a + 13591409)
            else:
                m = (a + b) // 2
                Pam, Qam, Ram = binary_split(a, m)
                Pmb, Qmb, Rmb = binary_split(m, b)
                Pab = Pam * Pmb
                Qab = Qam * Qmb
                Rab = Qmb * Ram + Pam * Rmb
            return Pab, Qab, Rab

        # main
        print("\nThe π Calculator\nMethod: Chudnovsky Algorithm\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        start_time = time()
        getcontext().prec = digits + 4
        if getcontext().Emax < digits ** 2:
            getcontext().Emax = digits ** 2
        if digits + 4 < 28:
            P, Q, R = binary_split(1, 2)
        else:
            from math import ceil
            P, Q, R = binary_split(1, ceil((digits + 5) / 14))
        del P
        result += "π: " + str((426880 * Decimal(10005).sqrt() * Q) / (13591409 * Q + R))[:digits + 2]
    elif calculation_option == "b":
        # √2

        # main
        print("\nThe √2 Calculator\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        start_time = time()
        getcontext().prec = digits + 4
        result += "√2: " + str(Decimal(2).sqrt())[:digits + 2]
    elif calculation_option == "c":
        # e

        # imports
        from fractions import Fraction
        from math import ceil

        # define variables
        factorial = 1
        e = 0
        end_fact = 2

        # main
        print("\nThe e Calculator\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        start_time = time()
        getcontext().prec = digits + 4
        if getcontext().Emax < digits ** 2:
            getcontext().Emax = digits ** 2
        inv_fact = Decimal("2e" + str(digits))
        while inv_fact != 1:
            inv_fact = Decimal(ceil(inv_fact / end_fact))
            end_fact += 1
        for i in range(1, end_fact):
            e += Fraction(1, factorial)
            factorial *= i
        result += "e: " + str(Decimal(e.numerator) / e.denominator)[:digits + 2]
    elif calculation_option == "d":
        # φ

        # main
        print("\nThe φ Calculator\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        if digits < 1:
            raise ValueError
        start_time = time()
        getcontext().prec = digits + 4
        if getcontext().Emax < digits ** 2:
            getcontext().Emax = digits ** 2
        result += "φ: " + str((1 + Decimal(5).sqrt()) / 2)[:digits + 2]
    else:
        raise ValueError
except ValueError:
    error += "VALUE ERROR: Invalid value."
    start_time = time()
except MemoryError:
    error += "MEMORY ERROR: Not enough memory to complete calculation."
    start_time = time()
except Exception as e:
    error += "UNKNOWN ERROR: " + str(e)
    start_time = time()
end_time = time()
result_list = []
if error == "\n":
    result += "\n\n"
    for i in range(0, len(result), 10000):
        result_list.append(result[i:i + 10000])
    for fragment in result_list:
        print(fragment)
        sleep(0.05)
    sleep(0.95)
    print("Total calculation time: " + str(end_time - start_time) + " seconds\n\n")
else:
    print(error + "\n\n")
sleep(1)
input("Press Enter to exit...")