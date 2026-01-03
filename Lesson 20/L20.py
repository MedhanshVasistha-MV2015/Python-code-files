from datetime import date , time , datetime
today = date.today()
now = datetime.now()
print('Todays day is: ' , today)
print('The time is: ' , now)
print('The date components are: ' , today.year , today.month , today.day )