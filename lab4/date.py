#1:
import datetime
new_datetime = datetime.datetime.now() - datetime.timedelta(days=5)
print(new_datetime)

#2:
import datetime
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
tomorrow = now + datetime.timedelta(days=1)
print(yesterday)
print(now)
print(tomorrow)

#3:
import datetime
x = datetime.datetime.now()
print(x.strftime("%f"))

#4:
import datetime
date1 = datetime.datetime(2024, 2, 10, 12, 30, 0)
date2 = datetime.datetime(2024, 2, 15, 14, 45, 0)
difference = date2 - date1
print(difference.total_seconds())




