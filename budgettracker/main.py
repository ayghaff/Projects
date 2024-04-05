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
        return True

def main():
    with open(r"firstuse.txt", "r") as file:
        lines = file.readlines()

    checking = check_first_use(lines)
    print(checking)

    if checking:
        firstuse.start_up()
    else:
        pass

    tracker.tracker()


if __name__ == "__main__":
    main()
