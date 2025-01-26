while True:
    try:
        lower_bound = int(input("Enter the lower bound: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        upper_bound = int(input("Enter the upper bound: "))
        break
    except ValueError:
        print("Please enter a valid number")

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(lower_bound, upper_bound + 1):
    if check_prime(num):
        primes.append(num)
        print(num)

if primes:
    prime_average = sum(primes) / len(primes)
    print(prime_average)
else:
    print("No primes found in the range.")