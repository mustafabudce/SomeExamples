first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if first_number % second_number == 0:
    print('{} is a multiple of {}'.format(first_number, second_number))

else:
    print('{} is not a multiple of {}'.format(first_number, second_number))

