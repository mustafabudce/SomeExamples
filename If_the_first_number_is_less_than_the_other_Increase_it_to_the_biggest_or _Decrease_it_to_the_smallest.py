first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if first_number < second_number:
    for i in range(first_number, second_number + 1, +1):
        print(i)
else:
    for i in range(first_number, second_number - 1, -1):
        print(i)
