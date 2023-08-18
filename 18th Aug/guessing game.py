#python program to guess a number in a given range
import random
a = random.randint(0, 50)
i = False
count = 0
while not i:

    guess = int(input("Enter a number in the range (0-50): "))
    if guess < 0 or guess > 50:
        print("Out of range!")
    else:
        if guess > a:
            print("High, enter a smaller number.")
        elif guess < a:
            print("Low, enter a larger number. ")
        elif guess == a:
            print("You guessed it right! Congratulations!")
            i = True
    count= count+1
print("You guessed it in", count, "guesses")
