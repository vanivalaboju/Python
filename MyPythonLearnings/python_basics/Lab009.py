# string - bunch or sequence of character represented by "" or ''
name = "harika"
name2 = 'Tapasya'
print(name)
print(type(name))
print(name2)
print(type(name2))

# raw string - it treats the backslash character(\) as a literal character
# it will be helpful in directory paths
dir = r"C:/Users/aravindkathiroju/Documents"
print(dir)
# dir2 = "C:\Users\tapasya\Documents" # it gives a syntax error due to \t(escape character)
# print(dir2)
dir3 = "C:\\Users\\tapasya\\Documents" # it prints o/p because we are using \\ instead of raw string
print(dir3)

# Format string - {var name} replaces its value
first_name = "vani"
last_name = "kathiroju"
age = 34
isMarried = True
print(f"My name is {first_name} {last_name}",f"my age is {age}",f"i am married {isMarried}",sep="\n")