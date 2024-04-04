import csv
import firstuse
import view
import add

def tracker():
    command_list = ["add", "remove", "view", "tutorial"]
    while True:
        print("Would you like to add a budget or review your currently existing ones?")
        first_choice = input().lower()
        if not first_choice in command_list:
            print("Please type in a valid command to continue. You can also type 'tutorial' to go back to the tutorial")
            continue
        elif first_choice == "tutorial":
            print("tutorial")
            firstuse.start_up()
            continue
        elif first_choice == "remove":
            print("As of right now, the function for removing budgets is currently unavailable, and will have to be deleted manually within the file.")
            continue
        elif first_choice == "add":
            print("add")
        elif first_choice == "view":
            print("view")
        else:
            print("Please type in a valid command to continue. You can also type 'tutorial' to go back to the tutorial")
            continue
