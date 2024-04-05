def length_check(date):
    if "/" in date:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if not (1 <= m <= 12 and 1 <= d <= 31):
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
    month = month.zfill(2)  # Zero-fill if necessary
    day = day.zfill(2)
    year = year.zfill(4)  # Zero-fill year to 4 digits
    return f"{month}-{day}-{year}"


def outdated_long(date):
    month_list = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    format_date = date.strip().split()
    year = format_date[2]
    day = format_date[1].rstrip(",")
    month = month_list[format_date[0]]

    return f"{month}-{day.zfill(2)}-{year}"


def main(the_input):
    if "/" in the_input:
        if length_check(the_input):
            return outdated_short(the_input)
        else:
            raise ValueError("Invalid date format")
    elif "," in the_input:
        if length_check(the_input):
            return outdated_long(the_input)
        else:
            raise ValueError("Invalid date format")
    else:
        raise ValueError("Invalid date format")
