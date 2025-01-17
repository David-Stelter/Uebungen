try:
    import random

    def oberes_limit_bestimmen():
        while True:
            try:
                oberes_limit = int(input("Bitte geben Sie das obere Limit (>1) ein: "))
                if oberes_limit <= 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Bitte gib eine Zahl größer als 1 ein.")
        return oberes_limit

    def random_number_generation(oberes_limit):
        return random.randint(1, oberes_limit)

    def get_user_guess():
        while True:
            try:
                guess = int(input("Bitte gib deine Tipp ein: "))
                if guess < 1 or guess > oberes_limit:
                    raise FileNotFoundError
                break
            except ValueError:
                print("Bitte gib eine Zahl ein.")
            except FileNotFoundError:
                print(f"Bitte gib eine Zahl über 0 und unter {oberes_limit + 1} ein.")
        return guess
    
    spiele = 0
    siege = 0
    niederlagen = 0
    siegesrate = 0
    while True: # Programm-Loop
        nutzer_tipp = 0
        versuche = 0
        spiele += 1
        oberes_limit = oberes_limit_bestimmen()
        computer_choice = random_number_generation(oberes_limit)

        while nutzer_tipp != computer_choice: # Game-Loop
            versuche += 1
            nutzer_tipp = get_user_guess()

            if nutzer_tipp != computer_choice and versuche <= 19:
                print(f"Das stimmt leider nicht. Du hast nocht {20 - versuche} Versuche.")
            elif nutzer_tipp != computer_choice and versuche >= 20:
                print("Das stimmt leider nicht und du hast keine Versuche mehr :(")
                niederlagen += 1
                break
            elif nutzer_tipp == computer_choice:
                print("Glückwunsch, du hast richtig geraten!")
                siege += 1


        if spiele != 1:
            if niederlagen != 0:
                siegesrate = siege / niederlagen
            else:
                siegesrate = siege
            if siegesrate % 1 == 0:
                print(f"Du hast bisher {siege} Spiele gewonnen und {niederlagen} Spiele verloren. \n Dadurch hast du eine Siegesrate von {int(siegesrate)}.")
            elif siegesrate % 0.5 == 0:
                print(f"Du hast bisher {siege} Spiele gewonnen und {niederlagen} Spiele verloren. \n Dadurch hast du eine Siegesrate von {siegesrate:.1f}.")
            else:
                print(f"Du hast bisher {siege} Spiele gewonnen und {niederlagen} Spiele verloren. \n Dadurch hast du eine Siegesrate von {siegesrate:.2f}.")


        weiter = input("Willst du nochmal spielen (n für nein, sonst weiter): ").lower()
        if weiter == "n":
            break
except KeyboardInterrupt:
    print("\n Tschüss")