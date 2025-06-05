age = input("Enter your age: ")
age = int(age)


if age >= 13:
    if age >= 8:
        print("You are eligible to create an account")
    else: 
        print("You are eligible to create an account but must be accompanied by an adult")
else:
    if age <= 3:
        print("How did you even type this?")
    else:
        print("You are not eligible to create an account")

print("End of program")