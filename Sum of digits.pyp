sum = 0

n = (input('Enter a number with multiple digits: '))

for x in n:
  sum = sum + int(x)

print('The addition of all digits in your number is ', sum)
