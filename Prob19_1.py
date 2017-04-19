import datetime
from calendar import monthrange
start=datetime.date(1901,1,1)
end=datetime.date(2001,1,1)
j=start
k=0
while(j!=end):
    if j.weekday()==6:
        k+=1
    j=j+datetime.timedelta(days=monthrange(j.year,j.month)[1])
print(k)

