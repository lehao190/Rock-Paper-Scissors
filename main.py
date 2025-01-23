## Game Goal: The player chooses rock, paper, or scissors, and the computer randomly selects one. Determine the winner based on the rules.
import random

options = ["rock", "paper", "scissors"]

# Ask the player for their choice (rock, paper, or scissors).
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate the input (ensure it’s one of the three options).
if user_choice not in options:
  print("Invalid choice. Please choose rock, paper, or scissors.")
  exit()

# Generate the computer’s choice randomly.
computer_choice = random.choice(options)

# Compare the player’s choice to the computer’s choice.
if user_choice == computer_choice:
  print("It's a draw!")
elif user_choice == "rock" and computer_choice == "scissors":
  print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
  print("You win!")
else:
  print("You lose!")

# Print the results.
print("You chose", user_choice)
print("The computer chose", computer_choice)