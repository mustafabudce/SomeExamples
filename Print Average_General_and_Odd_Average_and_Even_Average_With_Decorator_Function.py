def extra(func):
    def wrapper(numbers):
        total_even = 0
        count_even = 0
        total_odd = 0
        count_odd = 0
        for number in numbers:
            if number % 2 == 0:
                total_even = total_even + number
                count_even = count_even + 1
            else:
                total_odd = total_odd + number
                count_odd = count_odd + 1
        print("Average_odd:", total_odd / count_odd)
        print("Average_even:", total_even / count_even)

        func(numbers)
    return wrapper

@extra
def findAverage(numbers):
    total = 0
    for number in numbers:
        total = total + number
    print("Average_general:", total/len(numbers))
findAverage([1,2,30,40,5,41])