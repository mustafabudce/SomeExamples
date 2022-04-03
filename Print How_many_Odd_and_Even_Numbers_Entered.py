number_of_even_numbers = 0
number_of_odd_numbers = 0
for i in range(0, 5):
    number = int(input("Enter a number:"))
    if number % 2 == 0:
        number_of_even_numbers = number_of_even_numbers + 1
        print("even number")
        print("Entered number:", number)
        print("number_of_even_numbers:", number_of_even_numbers)

    else:
        number_of_odd_numbers = number_of_odd_numbers + 1
        print("odd number")
        print("Entered number:", number)
        print("number_of_odd_numbers:", number_of_odd_numbers)
    i = i + 1

