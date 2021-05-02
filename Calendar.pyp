import calendar as cd
import datetime as dt

x=int(input("Choose Year (number):"))
y=int(input("Choose Month (number):"))

print(cd.month(x,y))

f = dt.date(2014,7,2)
l = dt.date(2014,7,11)

xy = l - f

print(xy.days)
