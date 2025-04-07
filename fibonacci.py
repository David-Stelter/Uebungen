fibo1, fibo2 = 0, 1

while True:
    try:
        limit = int(input("Bitte geben Sie die Anzahl der Fibonacci-Zahlen ein, die Sie haben möchten: "))
        break
    except ValueError:
        print("Bitte gib eine ganze Zahl ein.")

for i in range(limit):
    if i == limit - 1:
        print(fibo1)
    else:
        print(fibo1, end="\n")
    fibo1, fibo2 = fibo2, fibo1 + fibo2