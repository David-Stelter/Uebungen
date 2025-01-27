import time

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def sieve_of_eratosthenes(lower_bound, upper_bound):
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    last_reported_percent = -1  # Start with an impossible percentage to ensure first report
    report_frequency = 0.1  # Report at least every 0.1 seconds for smoother feedback
    last_report_time = time.time()

    for i in range(2, upper_bound + 1):
        if is_prime[i]:
            if i >= lower_bound:
                primes.append(i)
            # Mark multiples of i as not prime
            for j in range(i * i, upper_bound + 1, i):
                is_prime[j] = False
            
            # Report progress
            current_percent = round(percent_done_function(lower_bound, upper_bound, i), 1)
            current_time = time.time()
            
            if current_percent > last_reported_percent or current_time - last_report_time > report_frequency:
                print(f"\r{current_percent}% done", end="", flush=True)  # Use \r for updating on the same line
                last_reported_percent = current_percent
                last_report_time = current_time

    print()  # Print a newline after the loop to move to the next line
    return primes

def percent_done_function(lower_bound, upper_bound, current_num):
    total = upper_bound - lower_bound
    done = current_num - lower_bound
    if total == 0:  # Avoid division by zero if lower_bound == upper_bound
        return 100
    return min(100, (done / total) * 100)

# Main execution
lower_bound = get_valid_integer("Enter the lower bound: ")
upper_bound = get_valid_integer("Enter the upper bound: ")

primes = sieve_of_eratosthenes(lower_bound, upper_bound)

if primes:
    prime_average = sum(primes) / len(primes)
    formattierter_durchschnitt = f"{prime_average:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    print(formattierter_durchschnitt)
else:
    print("No primes found in the range.")