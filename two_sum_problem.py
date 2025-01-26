import random
integers = []

while True:
    try:
        sum = int(input("Bitte geben Sie die Summe ein, die Sie erreichen möchten: "))
        break
    except ValueError:
        print("Bitte gib eine ganze Zahl ein.")

for i in range(sum):
    integers.append(i)

summands = []
for i in range(len(integers)):
    for j in range(i + 1, len(integers)):
        if integers[i] + integers[j] == sum:
            summands.append((integers[i], integers[j]))

for summanden in summands:
    print(f"{sum} = {summanden[0]} + {summanden[1]}")
if sum % 2 == 0:
    print(f"{sum} = {sum // 2} + {sum // 2}")