first_side = int(input("Enter the first side: "))
second_side = int(input("Enter the second side: "))
third_side = int(input("Enter the third side: "))
if first_side + second_side > third_side:
    if first_side + third_side > second_side:
        if second_side + third_side > first_side:
            print("This is a triangle")
        else:
            print("This is not a triangle")
    else:
        print("This is not a triangle")
else:
    print("This is not a triangle")
