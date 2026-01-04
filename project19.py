import calendar
try:
    yy = int(input("Enter the year: "))
    for mm in range(1,13):
        print(calendar.month(yy,mm))
except ValueError:
    print("Please enter a valid year.")