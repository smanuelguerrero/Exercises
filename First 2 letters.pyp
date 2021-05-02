xl = input('Enter a word: ')
if len(xl)<2:
  print(xl[:2]*2)
else:
  print(xl[:2]*len(xl))
