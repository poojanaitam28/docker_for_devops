# guessing_game.py
import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 100: ")
        attempts += 1
        try:
            guess = int(guess)
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()

