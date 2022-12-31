import datetime
import time

currentTime = datetime.datetime.now()
print(currentTime)

todayDate = datetime.datetime.today().date()
print(todayDate)
currentTimeIs = datetime.datetime.today().time()
print(currentTimeIs)
currentTime22 = datetime.datetime.today()
print(currentTime22)
time.sleep(1)
my_dateIs = datetime.datetime.today().strftime('%Y-%m-%d' + 'T' + '%H:%M:%S.%f')
print(my_dateIs)
my_dateIs = datetime.datetime.today().strftime('%Y%j%H%M%S')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y%j%H%M%S%z')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y%j%H%M%S%Z')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y-%b-%d')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y-%B-%d')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y-%B-%A')
print(my_dateIs)

my_dateIs = datetime.datetime.today().strftime('%Y-%B-%a')
print(my_dateIs)