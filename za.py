#Rock Paper Scissors Game
print("WELCOME TO THE ROCK PAPER SCISSORS GAME !")
choice = input("Enter your choice : ")
computer_choice = ["rock", "paper", "scissors"]
import random 
computer_choice = random.choice(computer_choice)

if (computer_choice == choice):
    print("Game draw")
elif(computer_choice == "rock" and choice == "paper"):
    print("You win") 
elif(computer_choice == "paper" and choice == "rock"):
    print("Computer win")
elif(computer_choice == "rock" and choice == "scissors"):
    print("Computer win")
elif(computer_choice == "scissors" and choice == "rock"):
    print("You win")
elif(computer_choice == "paper" and choice == "scissors"):
    print("You win")
elif(computer_choice == "scissors" and choice == "paper"):
    print("Computer Win")
else:
    print("Invalid choice")

