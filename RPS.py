#This is a rock paper scissors game  which allows the user to play against the computer
#This is very interesting game which almost all of us have played at some point in our childhood
#Let's Begin

import random

def select_gesture():
    user_input = input("Enter rock, paper, or scissors: ")
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        user_input = input("Enter rock, paper, or scissors: ")
    return user_input
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = select_gesture()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    permission = input("Do you want to play? (yes/no): ").strip().lower()
    if permission != "yes":
        print("Maybe next time. Goodbye!")
    else:
        while True:
            main()
            print("Thanks for playing!")
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again == "yes":
                continue
            elif again == "no":
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                again = input("Do you want to play again? (yes/no): ").strip().lower()
                
