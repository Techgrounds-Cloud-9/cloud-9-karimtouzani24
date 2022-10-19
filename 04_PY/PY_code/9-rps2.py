import random

user_wins = 0
computer_wins = 0
user_input = ""
computer_pick = ""
result = ""
options = ["rock", "paper", "scissors", "r", "p", "s"]

while True:
    user_input = input("Please use rock, paper or scissors: ")
    if user_input not in options:
        print("wrong input")
        continue
    else:
        break

print(f"the user_input is {user_input}")

def computer_move_function(computer_pick):
    print("The computer choose:", computer_pick)
    return computer_pick

computer_pick = random.choice(options)
computer_move_function(computer_pick)

def winner(user_input, computer_pick):
    if user_input == "rock" or "r":
        if computer_pick == "rock" or "r":
            result = "Tie"
        elif computer_pick == "paper" or "p":
            result = "computer_win"
        elif computer_pick == "scissor" or "s":
            result = "user_win"      
    elif user_input == "paper" or "p":
        if computer_pick == "rock" or "r":
            result = "user_win"
        elif computer_pick == "paper" or "p":
            result = "Tie"
        elif computer_pick == "scissors" or "s":
            result = "computer_win"
    elif user_input == "scissors" or "s":
        if computer_pick == "rock" or "r":
            result = "computer_win"
        elif computer_pick == "paper" or "p":
            result = "user_win"
        elif computer_pick == "scissors" or "s":
            result = "Tie"
    return result
    

result = winner(user_input, computer_pick)
print(f"The result is {result}")

            

   