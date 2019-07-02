# Pro/g/ramming Challenges
# 24: Rock,Paper, Scissors(+ lizard, Spock)
# by ahmad89098

import random

# un-comment all line from this point forward to play with lizard and spock as well.

weapons = ["Rock", "Paper", "Scissors"]#, "Lizard", "Spock"]
user_choice = input("Enter your choice: ")
com_choice = random.choice(weapons)

win = True

if user_choice == "Rock":
    if com_choice == "Paper": # or com_choice == "Spock":
        win = False
elif user_choice == "Paper":
    if com_choice == "Scissors": # or com_choice == "Lizard":
        win = False
elif user_choice == "Scissors":
    if com_choice == "Rock": # or com_choice == "Spock":
        win = False
# elif user_choice == "Lizard":
#     if com_choice == "Rock" or com_choice == "Scissors":
#         win = False
# elif user_choice == "Spock":
#     if com_choice == "Lizard" or com_choice == "Paper":
#         win = False

print("You chose: ", user_choice)
print("I chose: ", com_choice)
if user_choice == com_choice:
    print("Its a tie!")
elif win:
    print("You win!")
else: print("You lose!")