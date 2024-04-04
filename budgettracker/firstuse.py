def start_up():
    while True:
        enable_start_up = input("Hey! You seem new here! Would you like a guide on how to use the budget tracker?(y/n)")

        if enable_start_up == "yes" or enable_start_up == "y":
            input("Press enter to continue through the tutorial.")
            break
        elif enable_start_up == "no" or enable_start_up == "n":
            break
        else:
            print("Please input yes (y) or no (n)")
            continue
