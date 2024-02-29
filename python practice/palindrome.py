# Write a program to check if the given number is palindrome or not
# The Numbers that when reversed is the same as the original number itself are known as Palindromic Numbers.
def ispalindrome(num):
    if (num == num[::-1]):
        return "The number is a palindrome."
    else:
        return "The number is not a palindrome."


n = int(input("Enter the number:"))
print(ispalindrome(n))