import csv
test_data = [
    ['Name','Age','City'],
    ['Harika',34,'Hyderabad'],
    ['Veena',36,'Nebraska']
]

try:
    with open('mydata.csv','w') as file:
        writer = csv.writer(file)
        for data in test_data:
            writer.writerow(data)
except FileNotFoundError as f:
    print(f)
finally:
    print("close your files!")
    # close the file code