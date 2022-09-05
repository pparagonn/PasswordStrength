# Jovany Melchor
# ITMS 543 Vulnerability Analysis and Control
# This script is intended to assess whether a user's password is secure or not.
# This does require cracklib to be installed on the machine that this script is running on.
# A python3.7 or newer interpreter should be used
import subprocess
print("Hello, please enter a password.")
x = True

while x:
    password = input()
    if len(password) < 8:
        print("The length of the password needs "
              "to be 8 characters or greater")
        continue
    elif password.islower():
        print("Please place an uppercase letter "
              "in your password.")
        continue
    elif password.isupper():
        print("Please place a lowercase letter "
              "in your password.")
        continue
    elif not (any(char.isdigit() for char in password)):
        print("Please place a number in your "
              "password.")
        continue
    elif not (any(not char.isalnum() for char in password)):
        print("Please insert a symbol in "
              "your password.")
        continue
    else:
        x = False
process = subprocess.Popen(["cracklib-check", ], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, text=True)
process.stdin.write(password)
process.stdin.close()
print(process.stdout.read())
print("Password is valid.")
