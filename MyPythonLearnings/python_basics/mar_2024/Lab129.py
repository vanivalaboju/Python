#
with open("td.txt","r") as file:
    lines = file.readlines()
for line in lines:
    print(line,end="")
with open("td.txt",'a') as file:
    file.write("\n kamala is the mother of aravind")
