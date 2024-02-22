""" program to count vowels and consonants in a string.
vowels in english alphabet are 'a','e','i','o','u'.
All other alphabetic characters are considered as consonants."""

str1 = str(input("Enter the string:"))
vowels = 0
consonants = 0
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u' or
       i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U'):
       vowels = vowels + 1
    else:
       consonants = consonants + 1
print("Total number of vowels in this string = ", vowels)
print("Total number of consonants in this string = ", consonants)


