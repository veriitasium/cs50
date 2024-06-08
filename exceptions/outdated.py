import re

months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def convert_date(month, day, year):

    substitute_month = month
    if not month.isdigit():
        substitute_month = months[month]
        month = int(substitute_month)

    # if month not in months or (not 1 <= month <= 12):
    #     return ValueError

    # check whether day is in correct format and range
    if not day.isdigit():
        day = int(day)
        if not 1 <= day <= 31:
            return ValueError
    
    if not year.isdigit():
        year = int(year)
    

def format_date(month, day, year):    
    return f"{year}-{month:02}-{day:02}"
    


while True:
    try:
        month, day, year = re.split(' |/|, ', input("Date: "))
        convert_date(month, day, year)

        print("Date:", format_date(month, day, year))
        break
    except ValueError:
        pass