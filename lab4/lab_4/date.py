from datetime import datetime, timedelta

now=datetime.now()

#1
res=now-timedelta(5)
print(res)

#2
yesterday=now-timedelta(1)
tomorrow=now+timedelta(1)
print(yesterday, now, tomorrow)

#3
result=now.replace(microsecond=0)
print(result)

#4
now= datetime.now()
a=now-timedelta(10)

diff=a-now
sec=diff.total_seconds()

print(sec)