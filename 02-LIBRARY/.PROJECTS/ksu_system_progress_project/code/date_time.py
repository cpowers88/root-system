import datetime


def date_time_now():
    now = datetime.datetime.now()
    return now


print(f("Date: "),date_time_now().strftime("%Y-%m-%d")))
print(date_time_now().strftime("%H:%M:%S"))
