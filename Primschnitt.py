def get_valid_integer(prompt): # Stellt sicher, dass upper bound und lower bound Integer sind.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")

def sieve_of_eratosthenes(lower_bound, upper_bound):
    is_prime = [True] * (upper_bound + 1) # Liste mit n Elemente, alle vorerst wahr (Primzahl)
    is_prime[0] = is_prime[1] = False # 0 und 1 sind keine Primzahlen, werden also auf False geändert
    primes = [] # Initialisiere Liste mit Primzahlen, noch leer

    for i in range(2, upper_bound + 1): # for-Schleife die von 2 (der ersten Primzahl) bis inklusive upper_bound läuft
        if is_prime[i]:
            if i >= lower_bound:
                primes.append(i) # Wenn is_prime[i] = True, und größer oder gleich dem lower bound ist, wird i der Liste an Primzahlen hinzugefügt

            for j in range(i * i, upper_bound + 1, i):
                is_prime[j] = False # Alle vielfachen von i werden auf False gesetzt, da sie mindestens durch drei Zahlen teilbar sind, 1, i und x * i, wobei x eine natürliche Zahl ist
            # Man beginnt bei i * i weil alle anderen schon False sind, da sie ein Ergebnis von k * i sind, wobei k < i. Da man von unten nach oben vorgeht, hat man alle vielfachen von k schon False markiert.
            
    return primes

while True: # Stellt sicher, dass lower_bound < upper_bound
    lower_bound = get_valid_integer("Gib die untere Grenze ein: ")
    upper_bound = get_valid_integer("Gib die obere Grenze ein: ")

    if lower_bound >= upper_bound:
        print("Bitte stelle sicher, dass die untere Grenze kleiner ist als die obere Grenze.")
    else:
        break

primes = sieve_of_eratosthenes(lower_bound, upper_bound)

if primes:
    print(f"Die Primzahlen von {lower_bound} bis {upper_bound} sind folgende:") # Gibt alle Primzahlen aus
    for i in range(len(primes)):
        print(f"- {primes[i]}")

    prime_average = sum(primes) / len(primes) # Ermittelt den Durchschnitt der Primzahlen
    formattierter_durchschnitt = f"{prime_average:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') # Formattiert die Primzahlen in das Format 1.000,00
    
    print(f"Der Durchschnitt aller Primzahlen von {lower_bound} bis {upper_bound} ist {formattierter_durchschnitt}")
else:
    print(f"Zwischen {lower_bound} und {upper_bound} gibt es keine Primzahlen.")