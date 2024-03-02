# try,except and finally block
# multiple exception
try:
    num1 = int(input("Enter a number 1\n"))
    num2 = int(input("Entre a number 2\n"))
    result = num1 / num2
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result {result}")
finally:
    print("I will be executed anyhow!")

# ValueError means i can enter other than integer
# invalid literal for int() with base 10: 'harika'
# ZeroDivisionError means a value 12 b as zero