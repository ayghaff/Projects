import csv
import datecheck

def ask_for_input():
    while True:
        try:
            date = input("Date: ")
            date = datecheck.main(date)
            print(date)
        except ValueError:
            print("Please insert a valid date.")
            continue
        break
    while True:
        amount = input("Amount: ").lstrip("$")
        try:
            float(amount)
        except ValueError:
            print("Please input a valid number.")
            continue
        break
    category = input("Category: ")

    track_input = [date, amount, category]
    return track_input

def main():
    with open("tracker.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        track_input = ask_for_input()
        track_input[1] = f"${float(track_input[1]):.2f}"
        writer.writerow(track_input)

if __name__ == "__main__":
    main()
