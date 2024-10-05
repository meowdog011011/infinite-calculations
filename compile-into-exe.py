# This file compiles Infinite Calculations into an executable

# imports
from subprocess import run

# main
result = run("py -m pip install -U pyinstaller")
if result.returncode == 0:
    print("Successfully installed PyInstaller.")
    result = run("pyinstaller infinite-calculations.spec")
    if result.returncode == 0:
        print("Successfully installed Infinite Calculations.")
    else:
        print("ERROR: An error occured while trying to compile Infinite Calculations. Please check that all files are in their original locations and try again later.")
        exit(1)
else:
    print("ERROR: An error occured while trying to install PyInstaller. Please check that you have installed pip and try again later.")
    exit(1)
user_input = input("Would you like to uninstall the required dependency, PyInstaller? (Y/N) ").lower()
if user_input == "y":
    result = run("py -m pip uninstall pyinstaller")
    if result.returncode == 0:
        print("Successfully uninstalled PyInstaller.")
    else:
        print("ERROR: An error occured while trying to uninstall PyInstaller. Please try again later.")
        exit(1)