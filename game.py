import random

secret_number = random.randint(200,500)
guess = input("What's your guess?")
incorrect = True

while incorrect:
    try:
        int(guess) 
        if int(guess) > secret_number:
            print("too big")
            guess = input("What's your guess? ")
        elif int(guess) < secret_number:
            print("too small")
            guess = input("What's your guess? ")
        else:
            print("you win!")
            incorrect = False
    except:
        print("invalid input, please fill in a number")
    
    