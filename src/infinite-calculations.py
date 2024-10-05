# imports
from time import sleep

# configure print() to always forcibly flush
orig_print = print
def print(string: str):
    orig_print(string, end = "", flush = True)

# main
print("Welcome to Infinite Calculations\nVersion: 0.1.0-beta\nCreated by Te Du\n\n")
sleep(1)
print("What would you like to calculate?\n(A) π: Chudnovsky Algorithm\n(B) π: Gosper's series\n(C) √2\n(D) Fibonacci Sequence\n\n")
sleep(1)
try:
    user_input = input("Type A, B, C or D: ").lower()
    print("\n")
    if user_input == "a":
        # π: Chudnovsky Algorithm
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
        print("\nπ: " + str(pi)[:digits + 2] + "\n")
    elif user_input == "b":
        # π: Gosper's series

        # imports
        from asyncio import get_event_loop, sleep as async_sleep, create_task, CancelledError, run
        # define main and Enter key handler
        async def async_input(prompt):
            loop = get_event_loop()
            return await loop.run_in_executor(None, input, prompt)
        async def print_pi():
            q = 60
            r = 13440
            t = 10080
            i = 3
            await async_sleep(1)
            print("\n\nπ: ")
            await async_sleep(0.1)
            print("3")
            await async_sleep(0.1)
            print(".")
            while True:
                await async_sleep(0.1)
                digit = ((i * 27 - 12) * q + r * 5) // (t * 5)
                print(digit)
                u = i * 3
                u = (u + 1) * 3 * (u + 2)
                r = u * 10 * (q * (i * 5 - 2) + r - t * digit)
                q *= 10 * i * (i * 2 - 1)
                i += 1
                t *= u
        async def main():
            printing_pi = create_task(print_pi())
            await async_input("Press Enter to stop...")
            printing_pi.cancel()
            try:
                await printing_pi
            except CancelledError:
                pass

        # main
        print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\n")
        sleep(1)
        run(main())
    elif user_input == "c":
        # √2
        from decimal import Decimal, getcontext

        # set variables
        x_n = Decimal(1)

        # main
        print("Infinite Calculations: The √2 Calculator\nMethod: Newton's algorithm\n\n")
        sleep(1)
        digits = int(input("How many digits would you like to calculate? "))
        getcontext().prec = digits + 4
        precision = Decimal(1) / Decimal("1e+" + str(digits + 1))
        while True:
            x_next = (x_n + 2 / x_n) / 2
            if abs(x_next - x_n) < precision:
                break
            x_n = x_next
        print("\n√2: " + str(x_next)[:digits + 2] + "\n")
    elif user_input == "d":
        # Fibonacci Sequence

        # set variables
        fib = [0, 1]

        # main
        print("Infinite Calculations: The Fibonacci Calculator\n\n")
        sleep(1)
        digits = int(input("How many terms would you like to calculate? "))
        if digits < 1:
            raise ValueError
        print("\nFibonacci Sequence: ")
        if digits < 3:
            for i in range(digits):
                print(fib[i])
                if i != digits - 1:
                    print(", ")
        else:
            print("0, 1, ")
            for i in range(digits - 2):
                fib.append(fib[0] + fib[1])
                print(fib[-1])
                if i != digits - 3:
                    print(", ")
                del fib[0]
        print("\n")
    else:
        raise ValueError
except ValueError:
    print("\nERROR: Invalid value.")
except MemoryError:
    print("\nERROR: Not enough memory to complete process.")
sleep(1)
input("\nPress Enter to exit...")