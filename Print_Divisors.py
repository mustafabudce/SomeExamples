def findDivisor(number):
    divisors = []
    number = int(input("Enter a number :"))
    for divisor in range(2, number):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors
result = findDivisor(number = 'number')
print(result)
