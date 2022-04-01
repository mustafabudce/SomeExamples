integer = int(input("Enter a integer:"))

if integer == 0:
    print("Enter a integer other than zero")
    integer = int(input("Enter a integer:"))
if integer > 0:
    print("Integer is positive")
elif integer < 0:
    print("Integer is negative")
    