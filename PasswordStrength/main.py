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
print("Password is valid.")
