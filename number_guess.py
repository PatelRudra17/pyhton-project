import random

top_of_range = input("Type a number:")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 ")
        quit()
    else:
        print("You have entered a valid number")

random_number = random.randrange(0 , top_of_range)
guesses = 0 # number of guesses
max_guesses = max(1, top_of_range // 2) # maximum number of guesses
print(f"you will get {max_guesses} guesses") # f-string use 

while guesses < max_guesses:
    user_guess = input("Make a gusess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1 # increment the number of guesses
    else:
        print("Please type a number")
        continue
    if user_guess == random_number:
        print("You got it", guesses, "guesses") 
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

    if guesses == max_guesses and user_guess != random_number:
        print("You lose, the number is", random_number)




    
    