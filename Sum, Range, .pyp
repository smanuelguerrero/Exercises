a=int(input("Enter a value: "))
b=int(input("Enter a value: "))
c=int(input("Enter a value: "))

if a==b or a==b or b==c:
  print(int(0))
else:
  print(int(a+b+c))
  
# Example 2

a=int(input("Enter a value: "))
b=int(input("Enter a value: "))

if a+b in range(15,20):
  print(int(20))
else:
  print(int(a+b))
  
# Example 3

a=int(input("Enter a value: "))
b=int(input("Enter a value: "))

for sum in (a,b):
  if a == b:
    print(True)
  elif a+b == 5:
    print(True)
  elif a-b == 5 or b-a == 5:
    print(True)
  else:
    print(a+b)
    
    
#Example 4

a=int(input("Enter a value: "))
b=int(input("Enter a value: "))

def sum(a,b):
  if a == b or abs(a-b) == 5 or (a+b) == 5:
    print(True)
  else:
    print(False, "Try to choose values that are the same or equal to 5")

sum(a,b)
