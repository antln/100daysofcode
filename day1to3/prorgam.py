from datetime import datetime
from datetime import date

print(datetime.today())

today = datetime.today()

print(type(today))

todaydate = date.today()

print(todaydate)

print(type(todaydate))

print(today.day)

christmas = date(2019, 12, 25)

print(christmas)

print(christmas - todaydate)

print((christmas - todaydate).days)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " days until Christmas. ")

else: print("Yay it's Christmas!")