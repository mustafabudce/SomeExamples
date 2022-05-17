import random
import time
print("""**********************
Guess Between 1 and 40.
**********************""")
random_number = random.randint(1, 40)
guess_right = 7

while True:
    your_guess = int(input("Your guess :"))
    if your_guess > random_number :
        print("Your guess is checking..")
        time.sleep(1)
        print("Please enter a small guess.")
        guess_right = guess_right - 1
    elif your_guess < random_number :
        print("Your guess is checking..")
        time.sleep(1)
        print("Please enter a bigger guess.")
        guess_right = guess_right - 1
    else :
        print("Congratulation. You won the game!!")
        break
    if guess_right == 0:
        print("You have no more guessing. And The game is over.")
        break




