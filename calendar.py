import time
import calendar
import datetime

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,3))

print(calendar.monthcalendar(2020,3)) 

print(calendar.calendar(2020))

day_of_week=calendar.weekday(2020,11,8)
print(day_of_week)

is_leep=calendar.isleap(2020)
print(is_leep)
