import datetime
import time

today = datetime.datetime.today()
print(today)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
