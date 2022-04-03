number = int(input("Enter a number between 0 to 1000: "))
if 0 <= number < 10:
    print(number, ":1 digits")
elif 10 <= number < 100:
    print(number, ":2 digits")
elif 100 <= number < 1000:
    print(number, ":3 digit")
else:
    print("You entered a number out of the range.Program is closing..")

