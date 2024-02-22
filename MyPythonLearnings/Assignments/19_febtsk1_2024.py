""" Program to check if two strings are Anagram
  An Anagram of a string is another string that contains same characters,
 only the order of characters can be different.
 example "abcd" and "dabc" are anagram of each other."""
# Function to check if two strings are anagram or not
def check(s1,s2):

# The sorted strings are checked
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
# User has to give input of two strings
# Driver code
s1 = str(input("Enter the first string:"))
s2 = str(input("Enter the second string:"))
result = check(s1,s2)
print(result)