## Sample 1
list1 = [3,9,5,6,7]
list2 = ["a",2.0, 8/3,12]

if 4 in list1 and list2:
  print( "a 4 was found in one of these lists" )
else:
  print("I couldn't find any 4 in these lists")
  
## Sample 2 
def list_count(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1
  return count

print(list_count([1,4,6,7,4])
print(list_count([1,4,6,4,7,4])
      
##Sample 3
op=[1,4,6,7,4]
plo=[1,4,6,4,7,4]

print(op.count(4))
print(plo.count(4))
