import cli
import gui
import sys


while True:
    prompt = input("Assuming you closed the window, would you like to use the CLI version? (y/n) ").lower()

    if not prompt:
        print("Please enter a valid method to continue, or you can type 'quit' or press 'CTRL + C' to quit the program")
        continue
    elif cli_mode := prompt == "y" or prompt == "yes":
        break
    elif i_wanna_quit_this_program_pls := prompt == "quit" or prompt == "no" or prompt == "n":
        break
    else:
        print("Please enter a valid method to continue, or press 'CTRL + C' to quit the program")
        continue

if cli_mode:
    cli.main()
elif i_wanna_quit_this_program_pls == "quit":
    sys.exit()