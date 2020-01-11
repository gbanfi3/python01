import random

highest = 10
answer = random.randint(1, highest)
print("ezt kell kitalálni: {}".format(answer))
print("guess a number between 1 and  {}".format(highest))
while True:
    guess = int(input("your guess: "))
    if guess == 0:
        print("vége")
        break
    elif guess < answer:
        print("guess higher")
    elif guess > answer:
        print("guess lower")
    else:
        print("eltaláltad")
        break
