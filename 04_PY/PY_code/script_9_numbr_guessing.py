import random

n = random.randint(0, 10)
print("The secret number is: ")
print(n)

while True:
    num_player = int(input("Please choose a number below 10: "))

    if num_player == n:
        print(num_player, "is the right number, well done.")
        break

    elif num_player < n:
        print("Wrong number. Please choose a higher number")

    else:
        print("Wrong number. Please choose a lower number")

        

