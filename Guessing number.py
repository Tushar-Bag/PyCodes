import random
a = random.randrange(1,10)
guess = int(input("Take a number: "))
while a!=guess:
    if guess < a:
        print("Ops! Chose a larger number:")
        guess = int(input("Take a number: "))
    elif guess > a:
        print("Ops! Chose a smaller number")
        guess = int(input("Take a number: "))
else:
    print("You got it")
