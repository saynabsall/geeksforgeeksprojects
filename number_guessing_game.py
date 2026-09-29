import random
attempts = 7

def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")

def play_game(number, attempt=1):
    if attempt > attempts:
        print("\nGame over!")
        print("The correct number was: ", number)
        return

    guess = input(f"Attempt {attempt}/7 - Enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number. \n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100. \n")
        return play_game(number, attempt)

    check_guess = lambda x, y: "correct" if x == y else ("low" if x < y else "high")

    result = check_guess(guess, number)

    if result == "correct":
        print("\nCongratulations! You guess the correct number!")
        print("You guessed it in", attempt, "attempt(s).")
        return
    if result == "low":
        print("Too low! Try a higher number. \n")
    else:
        print("Too high! Try a lower number. \n")

    play_game(number, attempt + 1)

display_rules()
random_number = random.randint(1,100)
play_game(random_number)