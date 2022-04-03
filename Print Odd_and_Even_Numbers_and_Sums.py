number_of_digits = int(input("How many numbers to enter :"))
print("Please enter only integer")

number_of_odd_numbers = 0
sum_of_odd_numbers = 0
number_of_even_numbers = 0
sum_of_even_numbers = 0

for i in range(0, number_of_digits) :
    number = int(input())
    if number % 2 == 0:
        number_of_even_numbers = number_of_even_numbers + 1
        sum_of_even_numbers = sum_of_even_numbers + number
    else:
        number_of_odd_numbers = number_of_odd_numbers + 1
        sum_of_odd_numbers = sum_of_odd_numbers + number

print("number_of_even_numbers:", number_of_even_numbers)
print("sum_of_even_numbers:", sum_of_even_numbers)
print("number_of_odd_numbers:", number_of_odd_numbers)
print("sum_of_odd_numbers:", sum_of_odd_numbers)
