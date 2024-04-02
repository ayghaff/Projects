import random

user_wins = 0
user_losses = 0

options = ["rock", "paper", "scissors"]

print("Press 'Q' to quit the program or 'M' to check your standings against the bot.")
while True:
    user_input = input("(R)ock, (P)aper, or (S)cissors?").lower()
    if user_input == "q":
        print("Bye!")
        quit()

    elif user_input == "m":
        print("You won", user_wins, "times, but lost", user_losses, "times.")
        print(":)")
        continue

    if user_input not in ["r", "p", "s"]:
        print("no")
        quit()

    random_number = random.randint(0,2)
    #0r,p1,s2
    bot_pick = options[random_number]
    print("Bot chose", bot_pick + ".")

    if user_input == "r" and bot_pick == "scissors":
        print("Nice, you won!")
        user_wins += 1

    elif user_input == "p" and bot_pick == "rock":
        print("Thou has defeated the so called 'rock'!")
        user_wins += 1

    elif user_input == "s" and bot_pick == "paper":
        print("The paper has been shredded. So you won.")
        user_wins += 1

    else:
        print("Game over")
        user_losses += 1

print("You won", user_wins, "times, but lost", user_losses, "times.")
print(":)")