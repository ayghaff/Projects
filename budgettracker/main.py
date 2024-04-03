import csv
import firstuse

def check_first_use(lines):
    try:
        check_first_use = lines[1]
        if check_first_use == "false":
            return False
        else:
            return True
    except IndexError:
        print("not exist")
        return True

with open("firstuse.txt", "r") as file:
    lines = file.readlines()

checking = check_first_use(lines)
print(checking)

if checking == "true":
