import os
import sys
import subprocess
import time
import platform
from main import monoomaOS
import platform
def monoma_math():
    if platform.system() == "Windows":
        os.system('title monomaOS v0.0.1')
    else:
        os.system('echo -n -e "\033]0;monomaOS v0.0.1\007"')
    print("what math do you want to do?")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    math_choice = input("Enter your choice: ")
    if math_choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if math_choice == "1":
            print(f"Result: {num1 + num2}")
            time.sleep(2)
            print("endering back to monomaOS...")
            monoomaOS()
        elif math_choice == "2":
            print(f"Result: {num1 - num2}")
            time.sleep(2)
            print("endering back to monomaOS...")
            monoomaOS()
        elif math_choice == "3":
            print(f"Result: {num1 * num2}")
            time.sleep(2)
            print("endering back to monomaOS...")
            monoomaOS()
        elif math_choice == "4":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
                time.sleep(2)
                print("endering back to monomaOS...")
                monoomaOS()
            else:
                print("Error: Division by zero is not allowed.")
                time.sleep(2)
                print("endering back to monomaOS...")
                monoomaOS()
    else:
        print("Invalid choice. Returning to main menu...")
        time.sleep(2)
        print("endering back to monomaOS...")
        time.sleep(2)
        monoomaOS()

