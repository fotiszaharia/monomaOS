from main import monoomaOS
import platform
import os
if platform.system() == "Windows":
    os.system('title monomaOS v0.0.1')
else:
    os.system('echo -n -e "\033]0;monomaOS v0.0.1\007"')
print("welcome to monomaOS")
input("Press enter to continue...")
monoomaOS()
