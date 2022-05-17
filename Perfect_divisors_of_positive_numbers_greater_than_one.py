def divisible_number(number):
    divisible_number = []
    for i in range(2, number + 1):
        if number % i == 0:
            divisible_number.append(i)
    return divisible_number
while True :
    number = int(input("Enter the number or for exit(0) :"))
    if number == 0:
        print("Program is Closing...")
        break
    elif number == 1:
        print("Please enter different than one")
    else:
        print("Divisible Numbers :", divisible_number(number))



