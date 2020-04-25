import datetime

today=datetime.datetime.now()
print(today)

today.strftime('%B %d, %Y')
print(today)

#date_time_thing=datetime.datetime.strptime('March 09,2019','%B %d, %Y')
#print(datetime_thing)


birthday=datetime.date(1997,11,12)
print(birthday)#Object

day_since_birth=(today-birthday).days
print(day_since_birth)

tdelta=datetime.timedelta(days=10)
print(today+tdelta)

print(today.month)

print(today.day)

print(today.weekday())

print(datetime.time(7,2,20,15))

hour_delta=datetime.timedelta(hours=10)
print(datetime.datetime.now()+hour_delta)

#datetime_today=datetime.datetime.now(tz=pytz.UTC)
#datetime_pecific=datetime_today.astimezone(pytz.timezone('US/Pacific'))
#print(datetime_pecific)
