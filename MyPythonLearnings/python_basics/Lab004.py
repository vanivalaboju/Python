# Identifier means variable name(Aa-Zz,0-9,_) = variable value(it can be of different types)
age,name,size,complex = 40,'v',12.5,1+3j
print(age,name,size,complex,sep=',')
# 234 = 385 varname cant start with numbers
_123 = 345 # varname starts with variable name
print(_123)
# $890 ="siri" we cant have $ as a variable name
_ = "Athulith" # we can _ as a variable name also
print("Athulith")
# both varname are different both have different containers to store values
age = 34
print(age)