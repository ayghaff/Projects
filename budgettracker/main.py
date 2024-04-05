import csv
import firstuse
import tracker

def check_first_use(lines):
    try:
        check_first_use = lines
        if "false" in check_first_use:
            return False
        else:
            return True
    except IndexError:
        print("not exist")
        return True

def main():
    with open(r"budgettracker\firstuse.txt", "r") as file:
        lines = file.readlines()

    checking = check_first_use(lines)
    print(checking)

    if checking:
        print("work")
        firstuse.start_up()
    elif not checking:
        print("work but fals")
    else:
        print("no work")

    tracker.tracker()


if __name__ == "__main__":
    main()
