from datetime import date
from datetime import time
from datetime import datetime

#create a timestamp
t = time(11,25,59)
print t
print t.hour
print t.minute
print t.second

#todays date
d = date.today()
print d
print d.month
print d.year
print d.day
d1 = d.replace(year=2017)
print d1

#date and time now
now = datetime.now()
print now

#date and time utc now
utcNow = datetime.utcnow()
print utcNow

#time now
nowTime = datetime.now().time()
print nowTime
