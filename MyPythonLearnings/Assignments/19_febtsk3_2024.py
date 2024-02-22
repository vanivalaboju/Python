# Program to find a substring in a string
# The in operator is used to test whether a particular value (substring) exists within a sequence.

string = str(input("Enter the string:"))
sub_str = str(input("Enter the word:"))
if(string.find(sub_str)==-1):
    print("substring not found in string!")
else:
    print("substring in string!")

