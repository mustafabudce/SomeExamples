number = input("Please enter a number greater than zero:")

for x in range(0, int(number)):
    if int(x) % 2 == 0:
        print(int(x), ": even number")
    else:
        if int(x) % 2 != 0:
            print(int(x), ": odd number")


