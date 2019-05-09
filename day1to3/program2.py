from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(type(t))

print(t.days)

print(t.seconds)

print(t.seconds / (60*60))

eta = timedelta(hours=6)

today = datetime.today()

print(today)

print("eta : " + str(eta))

print(str(today + eta) )