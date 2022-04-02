
print("***********  Welcome to Calculator ***********")
option1 = "(1)Addition"
option2 = "(2)Subtraction"
option3 = "(3)Multiplication"
option4 = "(4)Division"

print(option1)
print(option2)
print(option3)
print(option4)
print("Please choose one of the options..")
option_number = input("Enter the option number: ")

while True:
    if option_number == "1":
        number1 = input("Enter the first number:")
        number2 = input("Enter the second number:")
        print(number1, "+", number2, "=", int(number1) + int(number2))
        break
    elif option_number == "2":
        number3 = input("Enter the first number:")
        number4 = input("Enter the second number:")
        print(number3, "-", number4, "=", int(number3) - int(number4))
        break
    elif option_number == "3":
        number5 = input("Enter the first number:")
        number6 = input("Enter the second number:")
        print(number5, "*",number6, "=", int(number5) * int(number6))
        break
    elif option_number == "4":
        number7 = input("Enter the first number:")
        number8 = input("Enter the second number:")
        print(number7, "/", number8, "=", int(number7) / int(number8))
        break
    elif option_number != 1 or option_number != 2 or option_number != 3 or option_number != 4:
        print("You entered a different selection number. Please enter only one of the option numbers.")
        option_number = input("Enter the option number: ")


