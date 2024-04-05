import csv
import datecheck

def main():
    with open("tracker.csv") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
