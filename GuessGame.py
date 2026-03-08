import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
number = random.randint(1, 100)


def compare(guess):
    compare_result = False
    if guess == number:
        print(f"You got it! The answer was {number}.")
        compare_result = True
    elif guess > number:
        print("Too high.")
        compare_result = False
    elif guess < number:
        print("Too low.")
        compare_result = False
    return compare_result

def game_mode(mode):
    if mode == 'easy':
        attempts = 10
    elif mode == "hard":
        attempts = 5
    else:
        print("Invalid Data404, You need to type 'easy' or 'hard'!!")
        game_mode(game_start)
    return attempts

def _main_():
    print(logo)
    continue_game = True
    game_start = input("Welcome to the Number Guessing Game!"
                      "\nI'm thinking of a number between 1 and 100."
                      "\nWhat game mode do you want to play? 'easy' or 'hard': ")
    attempts = game_mode(game_start)

    while continue_game:
        if attempts > 0:
            the_guess = int(input(f"You have {attempts} attempts remaining to guess the number."
                                  "\nMake a guess: "))
            result = compare(the_guess)
            if result == False:
                attempts -= 1
            else:
                print(f"You got it! The answer was {number}")
                continue_game = False
                _main_()
        else:
            print("You've run out of guesses.")
            continue_game = False
            if input("Do you want to play more? 'y' or 'n': ") == "y":
                print("\n" * 20)
                _main_()
            else:
                print("Goodbye!")

_main_()

