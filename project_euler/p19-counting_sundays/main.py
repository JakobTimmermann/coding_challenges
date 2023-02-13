days_in_month = {
    0: 31,  # Jan
    1: 28,  # Feb
    2: 31,  # Mar
    3: 30,  # Apr
    4: 31,  # May
    5: 30,  # Jun
    6: 31,  # Jul
    7: 31,  # Aug
    8: 30,  # Sep
    9: 31,  # Okt
    10: 30,  # Nov
    11: 31,  # Dez
}
weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday "}
first_day_of_month = 2
sundays_on_first = 0
for year in range(1, 101):
    if year % 4 == 0:
        print(f"Year {1900+year} was a leap year")
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    for month in range(12):
        if first_day_of_month == 0:
            sundays_on_first += 1
        first_day_of_month = (days_in_month[month] % 7 + first_day_of_month) % 7

print(sundays_on_first)