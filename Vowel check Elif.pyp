vowel = input("Enter a letter: ")

if vowel == 'a':
  print(vowel, " is a vowel!")
elif vowel == 'e':
  print(vowel, " is a vowel!")
elif vowel == 'i':
  print(vowel, " is a vowel!")
elif vowel == 'o':
  print(vowel, " is a vowel!")
elif vowel == 'u':
  print(vowel, " is a vowel!")
else:
  print("This is not a vowel")
  
  
 #2nd example

letter = input("Please enter a letter: ")
vowels = ("A", "E", "I", "O", "U")

if letter in vowels:
  print("Your letter is a vowel.")
else:
  print("Your letter is not a vowel.")
