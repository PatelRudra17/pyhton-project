print("welcome to my quiz game")

playing = input("Do yoy want to play? (yes /no): ")
if (playing != "yes"):
    print("ok , maybe next time : ")
    quit()
else:
    print("ok lets play :\n")

name = input("enter your name : ")
print("welcome", name, "to the game \n")

print("here are some rules before we start :")
print("1. Each correct answer gives you 1 point")
print("2. each wrong answer minus 1 point")
print("3. Type your answer in lowercase letters.")
print("4. You must answer every question.")
print("\n")
print("let's start the game :\n")

print("choose a category: ")
print("1. computer science")
print("2. general knowledge")
print("3. science")

category_choice = input("enter the category number (1/2/3) :")

categories = {
    "Computer Science": {
        "1. What does CPU stand for? ": "central processing unit",
        "2. What does RAM stand for? ": "random access memory",
        "3. What does ROM stand for? ": "read only memory"
    },
    "General Knowledge": {
        "1. Who is the Prime Minister of India (2025)? ": "narendra modi",
        "2. What is the capital of France? ": "paris",
        "3. Which planet is known as the Red Planet? ": "mars"
    },
    "Science": {
        "1. What is the chemical symbol for water? ": "h2o",
        "2. What gas do plants release during photosynthesis? ": "oxygen",
        "3. What is the nearest star to Earth? ": "sun"
    }
}

if category_choice == "1":
    category = "Computer Science"
elif category_choice == "2":
    category = "General Knowledge"
elif category_choice == "3":
    category = "Science"
else:
    print("invalid choice")
    quit()
    
score = 0

print(f"\n{category.upper()} Quiz \n")
questions = categories[category]

for q, a in questions.items():
    answer = input(q)
    if answer == a:
        print("correct")
        score += 1 
    else:
        print("incorrect")
        print("the correct answer is:",a)
        score -= 1
        print("your score is ", score, "\n")



print("your final score is ", score)





     
