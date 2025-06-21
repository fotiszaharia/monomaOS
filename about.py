from main import monoomaOS
import platform
import os
if platform.system() == "Windows":
    os.system('title monomaOS v0.0.1')
else:
    os.system('echo -n -e "\033]0;monomaOS v0.0.1\007"')


def about_mmonomaOS():
    print("monomaOS is a simple operating system written in Python.")
    print("It is designed to be easy to use and understand.")
    print("Version: 0.0.1")
    input("Press enter to enter back to monomaOS...")

    monoomaOS()
