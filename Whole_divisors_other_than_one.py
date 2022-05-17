def divisible_number(number):
    divisible_number = []
    for i in range(2, number + 1):
        if number % i == 0:
            divisible_number.append(i)
    return divisible_number
while True :
    number = int(input("Please enter the number or for exit(q):"))
    if number == "q":
        print("Program is Closing...")
        break
    else:
        print("Divisible Numbers :",divisible_number(number))



