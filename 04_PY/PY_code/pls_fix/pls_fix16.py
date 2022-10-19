import random

goal = random.randint(1, 100)

win = False
tries = 0

while win == False and tries < 7:
    try:
        inpt = int(input("Please input a number between 1 and 100: "))
        tries += 1

        if inpt == goal:
            win = True
            print("Congrats, you guessed the number!")
            print(f"It took you, {tries}, tries")
        elif inpt < goal:
            print("The number should be higher")
        else:
            print("The number should be lower")
    except:
        print("Please type an integer")

if win == False:
    print("Game over! You took more than seven tries")