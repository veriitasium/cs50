def main():
    breakfast_alert = "breakfast time"
    lunch_alert = "lunch time"
    dinner_alert = "dinner time"

    time = convert(input("What time is it? ").strip().lower())

    if 7. <= time <= 8.:
        print(breakfast_alert)
    elif 12. <= time <= 13.:
        print(lunch_alert)
    elif 18. <= time <= 19.:
        print(dinner_alert)

def convert(time_str):

    # period check
    if "a.m." in time_str or "p.m." in time_str:
        time, period = time_str.split()
        hours, minutes = map(float, time.split(":"))
    
        period = period.lower()
        if period == "p.m." and hours != 12:
            hours += 12
        if period == "a.m." and hours != 12:
            hours += 0
    else:
        hours, minutes = map(float, time_str.split(":"))
        
    return hours + (minutes/60.)


if __name__ == "__main__":
    main()