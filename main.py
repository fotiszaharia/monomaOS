# monomaOS v0.0.1
def monoomaOS():
    import os
    import sys
    import subprocess
    import platform
    import time
    import datetime
    from about import about_mmonomaOS    
    from monomaOS_math import monoma_math
    if platform.system() == "Windows":
        os.system('title monomaOS v0.0.1')
    else:
        os.system('echo -n -e "\033]0;monomaOS v0.0.1\007"')
    print("monomaOS v0.0.1")
    print("loading...")
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')  
    def run_command(command):
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
    while True:
        print("what do you want to do?")
        print("1. run a command")
        print("2. exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("what command do you want to run?")
            print("1. math")
            print("2. about monomaOS")
            print("3. back to main menu")
            comin = input("Enter your choice: ")
            if comin == "1":
                monoma_math()
            if comin == "2":
                about_mmonomaOS()

            elif comin == "3":
                print("Returning to main menu...")
                if os.name == 'nt':  # Windows
                    os.system('cls')
                else:  # Unix/Linux/MacOS
                    os.system('clear')
                sys.exit(0)

        elif choice == "2":
            print("Exiting monomaOS...")
            sys.exit(0)