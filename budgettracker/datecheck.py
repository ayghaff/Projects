
def length_check(date):
    if "/" in date:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if m > 12 or d > 31:
            return False
    elif "," in date:
        format_date = date.split()
        d = format_date[1].rstrip(",")
        if not d.isdigit() or int(d) > 31:
            return False
    else:
        return False
    return True


def outdated_short(date):

    month, day, year = date.strip().split("/")
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day
    returning_value = year,month,day, sep = "-"
    return returning_value


def outdated_long(date):
    month_list = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }

    format_date = date.strip().split()
    year = format_date[2]
    day = format_date[1].rstrip(",")
    month = month_list[format_date[0]]
    month = str(month)

    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day

    returning_value = year,month,day, sep = "-"
    return returning_value


def main(the_input):
    while True:
        try:
            date = the_input
            if "/" in date:
                if length_check(date) == False:
                    continue
                final_date = outdated_short(date)
                return final_date
                break
            elif "," in date:

                if length_check(date) == False:
                    continue
                final_date = outdated_long(date)
                return final_date
                break
            else:
                continue
        except ValueError:
            continue


if __name__ == "__main__":
    main(...)
