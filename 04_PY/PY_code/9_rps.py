valid_list = ["r", "rock", "p", "paper", "s", "scissors"]
input_player = ""

#function to validate the input.
def check_validation(input_player):
    while True:
        input_player = input("Please use rock, paper or scissors: ")
        if input_player not in valid_list:
            print("wrong input")
            continue
        else:
            break
    

input_player = input("Please choose rock, paper or scissors: ")
check_validation(input_player)
print("The player choose:", input_player)

#function to create a computer move.
import random
def move_computer(cp_move):
    print("The computer choose:", cp_move)
    return cp_move

cp_move = random.choice(valid_list)
move_computer(cp_move)

#function to check who won this round.
def winner(input_player, cp_move):
    if input_player == "rock" or "r":
        if cp_move == "rock" or "r":
            return "it is a tie"
        elif cp_move == "paper" or "p":
            return "computer wins"
        elif cp_move == "scissors" or "s":
            return "player wins"

    elif input_player == "paper" or "p":
        if cp_move == "rock" or "r":
            return "paper wins"
        elif cp_move == "paper" or "p":
            return "it is a tie"
        elif cp_move == "scissors" or "s":
            return "computer wins"

    elif input_player == "scissors" or "s":
        if cp_move == "rock" or "r":
            return "computer wins"
        elif cp_move == "paper" or "p":
            return "player wins"
        elif cp_move == "scissors" or "s":
            return "It is a tie" 
            
winner(input_player, cp_move)

user_wins = 0
computer_wins = 0

