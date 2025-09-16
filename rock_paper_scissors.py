import random
import winsound

name = input("Enter yourr name : ") 
print("hello", name, "welcome to rock Paper Scissors game")

user_win = 0
computer_win = 0 
draw = 0
options = ["rock", "paper", "scissors"]

user_history = []

def predict_next_move(user_history):

    if not user_history:
        return random.choice(options)
    most_common_move = max(set(user_history), key = user_history.count)
    if most_common_move == "rock":
        return "paper"
    elif most_common_move == "paper":
        return "scissors"
    else:
        return "rock"

while True:
    user_input = input("Enter rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2)
    computer_pick = options[random_num]

    print("computer picked", computer_pick)
    if user_input == "rock" and computer_pick == "scissors":
        print("you win")
        user_win += 1
        winsound.Beep(1000, 200)

    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_win += 1
        winsound.Beep(1000, 200)

    elif user_input == "scissors" and computer_pick == "paper":
        print("you win")
        user_win += 1
        winsound.Beep(1000, 200)

    elif user_input == computer_pick:
        print("it a draw")
        draw += 1
        winsound.Beep(500, 200)

    else:
        print("you lose")
        computer_win += 1
        winsound.Beep(200, 500)

        print("your socre is : ", user_win, "time" )
        print("you won", user_win, "times")
        print("computer won", computer_win, "times")
        print("draw", draw, "times")
    



