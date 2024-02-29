# Python Program to Check Prime Number
# To take input from the user
n = int(input("Enter the number:"))
if n == 1:
    print(n,"is not a prime number! ")
elif n > 1:
    # check for factors
    for i in range(2,n):
        if n % i == 0:
            print("number is not a prime number")
            print(i ,"times",n//i,"is",n)
            break
    else:
        print(n,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(n,"is not a prime number")