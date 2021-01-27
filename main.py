# Higher/Lower Game:

from game_data import data
from random import choice
from art import logo, vs
from replit import clear


# Function: Generate random account
def generate_random_account():
    """Get data from random account"""
    return choice(data)


# Function: Format data
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


# Function: Check answer
def check_answer(guess, a1_followers, a2_followers):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a1_followers > a2_followers:
        return guess == "a"
    else:
        return guess == "b"


# Function: Game
def game():
    print(logo)
    score = 0
    game_over = False
    account1 = generate_random_account()
    account2 = generate_random_account()

    # Keep game running if game not over
    while not game_over:
        account1 = account2
        account2 = generate_random_account()

        # Check if account1 is same as account2
        while account1 == account2:
            account2 = generate_random_account()

        # Print data to console
        print(f"Compare A: {format_data(account1)}.")
        print(vs)
        print(f"Against B: {format_data(account2)}.")

        # Let user guess the correct answer and check if correct
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a1_follower_count = account1["follower_count"]
        a2_follower_count = account2["follower_count"]
        is_correct = check_answer(guess, a1_follower_count, a2_follower_count)

        # Clear console
        clear()
        print(logo)

        # If correct answer, then increase score by 1 else print game over
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


# Run game
game()
