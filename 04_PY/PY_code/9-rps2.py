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

#function to check who wins the round
def winner(user_input, computer_pick):
    if user_input == "rock" or user_input == "r":
        if computer_pick == "rock" or computer_pick == "r":
            result = "Tie"
        elif computer_pick == "paper" or computer_pick == "p":
            result = "computer_win"
        elif computer_pick == "scissor" or computer_pick == "s":
            result = "user_win"      
    elif user_input == "paper" or user_input == "p":
        if computer_pick == "rock" or computer_pick == "r":
            result = "user_win"
        elif computer_pick == "paper" or computer_pick == "p":
            result = "Tie"
        elif computer_pick == "scissors" or computer_pick == "s":
            result = "computer_win"
    elif user_input == "scissors" or user_input == "s":
        if computer_pick == "rock" or computer_pick == "r":
            result = "computer_win"
        elif computer_pick == "paper" or computer_pick == "p":
            result = "user_win"
        elif computer_pick == "scissors" or computer_pick == "s":
            result = "Tie"
    return result
    

result = winner(user_input, computer_pick)
print(f"The result is {result}")

print(user_wins)
print(computer_wins)

def score(result, user_wins, computer_wins):
    if result == "user_win":
        user_wins += 1
        print(f"score user is now {user_wins}")
        return user_wins

    elif result == "computer_win":
        computer_wins += 1
        print(f"The score for the computer is now {computer_wins}")
        return computer_wins
        
        
score(result, user_wins, computer_wins)
print(f"The score is user {user_wins} and the computer {computer_wins}")
   