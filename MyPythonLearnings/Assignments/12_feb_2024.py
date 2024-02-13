# Create a function that checks if a given string is a palindrome
# palindrome :  A palindrome is a sequence of characters that, when reversed,
# would result in the exact same sequence of characters.

def ispalindrome(string):
     if(string == string[::-1]):
         return "The string is a palindrome."
     else:
         return "The string is not a palindrome."
str= input("Enter string:")
print(ispalindrome(str))