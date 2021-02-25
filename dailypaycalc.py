import datetime

saturdayRate = 0.5
sundayRate = 2

hoursStr = input("Hours Worked: ")
payrateStr = input("Hourly Payrate: ")
dateStr = input("Enter Date (DD/MM/YYYY): ")

day, month, year = dateStr.split("/")
dateInt = datetime.date(int(year), int(month), int(day))
weekday = dateInt.strftime("%A")

try:
    hours = float(hoursStr)
    payrate = float(payrateStr)
    if weekday == "Saturday":
        print(hours * (payrate * saturdayRate))
    elif weekday == "Sunday":
        print(hours * (payrate * sundayRate))
    else:
        print(hours * payrate)
except:
    print("Invalid character entered.")