import re
import string

print("Hello, please enter a password.")
password = input(String)
x = True

def run(password):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(password) == None):
        return True
    else:
        return False

while x:
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
    elif not(any(char.isdigit() for char in password)):
        print("Please place a number in your "
              "password.")
    elif not run:
        print("Please insert a symbol in "
              "your password.")
    








