def ndegrees(num):
  ans = True
  n, tempn, i =2,2,2,
  while ans:
    if str(tempn) in num:
      i+= 1
      tempn = pow(n,i)
    else:
      ans = False
    return i-1:
print(ndegrees('248'))
