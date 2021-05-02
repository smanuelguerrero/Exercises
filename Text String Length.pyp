isstring = str(input("Enter a word that is not is: "))

if len(isstring) >= 2 and isstring[:2] == "Is":
  print (isstring)
else:
  print( "Is" + isstring)


sample = input("Enter a word: ")

print(sample*len(sample))
