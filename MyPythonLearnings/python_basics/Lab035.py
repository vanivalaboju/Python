# Continue->it continues with the next iteration of the loop
for num in range(1,10):
    if num% 2 == 0:
        print(f"Found even number {num}")
        continue
    print(f"odd number {num}")

for i in range(1,10):
    if i % 3 == 0:
        print(i)
    else:
        print(i * 2)
    print("Hello")