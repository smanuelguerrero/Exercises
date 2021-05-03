import math as mt

x1 = float( input("Enter x1: ") )
x2 = float( input("Enter x2: ") )
y1 = float( input("Enter y1: ") )
y2 = float( input("Enter y2: ") )

d1 = float( (x2-x1)**2 )
d2 = float( (y2-y1)**2 )

sqrt = float( mt.sqrt(d1-d2) )

print(sqrt)
