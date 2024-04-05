import csv

def main():
    with open("tracker.csv") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        col_width = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

        print(' | '.join([str(item).ljust(width) for item, width in zip(rows[0], col_width)]), end='|')
        print('\n' + '-' * (sum(col_width) + len(rows[0]) + 1))  # Separator line

        for row in rows[1:]:
          print(' | '.join([str(item).ljust(width) for item, width in zip(row, col_width)]), end='|')
          print('\n')

if __name__ == "__main__":
    main()
