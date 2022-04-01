integer_first = int(input("Enter first integer:"))
integer_second = int(input("Enter second integer:"))
if integer_first == integer_second:
    print(integer_first, "equals", integer_second)
elif integer_first < integer_second:
    print(integer_second, "is greater than", integer_first)
else:
    print(integer_first, "is greater than", integer_second)
