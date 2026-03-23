# full project code for ethiopian holiday calendar exact date and name of the holiday
import datetime
def get_ethiopian_holiday_calendar(year):
    holidays = {
        "Enkutatash": datetime.date(year, 1, 1),
        "Meskel": datetime.date(year, 9, 27),
        "Timkat": datetime.date(year, 1, 19),
        "Genna": datetime.date(year, 1, 7),
        "Fasika": datetime.date(year, 4, 4),
        "Buhe": datetime.date(year, 8, 19),
        "Mariam": datetime.date(year, 11, 21)
    }
    return holidays
year = int(input("Enter the year to get the Ethiopian holiday calendar: "))
ethiopian_holidays = get_ethiopian_holiday_calendar(year)
print(f"Ethiopian Holiday Calendar for the year {year}:")
for holiday, date in ethiopian_holidays.items():
    print(f"{holiday}: {date.strftime('%B %d, %Y')}")
