import datetime

saturdayRate = 0.5
sundayRate = 2

try:
    hours = float(input("Hours Worked: "))
    payrate = float(input("Hourly Payrate: "))
    try:
        dateStr = input("Enter Date (DD/MM/YYYY): ")
        day, month, year = dateStr.split("/")
        dateInt = datetime.date(int(year), int(month), int(day))
        weekday = dateInt.strftime("%A")
        if weekday == "Saturday":
            print(hours * (payrate * saturdayRate))
        elif weekday == "Sunday":
            print(hours * (payrate * sundayRate))
        else:
            print(hours * payrate)
    except:
        print("Invalid date entered.")
except:
    print("Invalid character entered.")
