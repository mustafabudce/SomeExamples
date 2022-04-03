number = input("Enter the number:")
result = []
for a in range(2, int(number)):
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        result.append(a)
print(result)


