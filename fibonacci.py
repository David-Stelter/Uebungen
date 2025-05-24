def generate_fibonacci(limit):
    """
    Generates a list of Fibonacci numbers up to the given limit.
    """
    if limit <= 0:
        return []
    if limit == 1:
        return [0]

    fibo1, fibo2 = 0, 1
    fibonacci_numbers = []
    for _ in range(limit):
        fibonacci_numbers.append(fibo1)
        fibo1, fibo2 = fibo2, fibo1 + fibo2
    return fibonacci_numbers

if __name__ == "__main__":
    while True:
        try:
            user_limit = int(input("Bitte geben Sie die Anzahl der Fibonacci-Zahlen ein, die Sie haben möchten: "))
            break
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")

    results = generate_fibonacci(user_limit)

    for number in results:
        print(number)