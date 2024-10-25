import random


def game():
    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    result = f"Computer selected: {computer_choice}\n"

    # Ask the user to input their choice
    user_choice = input("Please enter your choice (rock, paper, scissors): ").lower()

    # Determine the winner
    if user_choice == computer_choice:
        result += "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        result += f"Congratulations! You win. {user_choice.capitalize()} beats {computer_choice}."
    else:
        result += f"Sorry, you lose. {computer_choice.capitalize()} beats {user_choice}."

    return result


# Example usage
game_result = game()
print(game_result)
