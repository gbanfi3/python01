import random

highest = 10
answer = random.randint(1, highest)

print("please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("guess higher")
    else:  # must be greater than number
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("sorry, not correct")
else:
    print("you got it first time")
