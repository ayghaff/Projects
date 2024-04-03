import random

def cli(min_number, max_number, playing, numlives):
    if numlives:
        lives = numlives
    else:
        lives = 3
    randomnum = random.randint(min_number, max_number)
    while True:
        if lives == 1:
            print(f"{lives} life left")
        else:
            print(f"{lives} lives left")

        try:
            user_guess = int(input("Insert your guess: "))
        except ValueError:
            print("Invalid value. Please insert an integer.")
            continue

        if user_guess > max_number:
            print("Please insert an integer within the inputted range.")
            continue
        elif user_guess < min_number:
            print("Please insert an integer within the inputted range.")
            continue

        if user_guess == randomnum:
            print(f"You guessed it! The number was {randomnum}!")
            while True:
                playcontinue = input("Would you like to play again? (y/n): ")
                if playcontinue == "y":
                    playing = True
                    return playing
                elif playcontinue == "n":
                    playing = False
                    return playing
                else:
                    print("Invalid input. Please enter a valid input.")
        elif lives > 1:
            lives -= 1
            continue
        else:
            print(f"You lost. The number was {randomnum}.")
            while True:
                playcontinue = input("Would you like to try again? (y/n): ").lower()
                if playcontinue == "y":
                    playing = True
                    return playing
                elif playcontinue == "n":
                    playing = False
                    return playing
                else:
                    print("Invalid input. Please enter a valid input.")
        

def main():
    while True:
        try:
            min_number = int(input("What would you like the minimum number to be?: "))
            max_number = int(input("What would you like the maximum number to be?: "))
            numlives = int(input("How many lives would you like to have?: "))
        except ValueError:
            print("Invalid value. Please insert an integer.")
            continue
        if min_number < 1 or max_number < 1:
            print("Please insert an integer greater than 0")
            continue
        if min_number > max_number:
            print("Please insert a minimum value less than your maximum value.")
            continue
        break
    
    playing = True
    while playing == True:
        playing = cli(min_number, max_number, playing, numlives)


if __name__ == "__main__":
    main()