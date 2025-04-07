from collections import Counter
worte = []

def ausführliche_ausgabe(wort_anzahl):
    for wort in wort_anzahl:
        print(f"'{wort}' kommt {wort_anzahl[wort]}-mal im Text vor.")

def kompakte_ausgabe(wort_anzahl):
    for wort in wort_anzahl:
        print(f"{wort}: {wort_anzahl[wort]}")

text = input("Geben Sie einen Text ein oder q wenn Sie einen Dateinamen eingeben wollen: ")
if text.lower() == "q":
    dateiname = input("Geben Sie den Dateinamen ein: ")
    with open(dateiname, "r") as datei:
        text = datei.read()
        datei.close()
text = text.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(")", "").replace("(", "").replace(":", "").replace(";", "").replace("„", "").replace("“", "").replace("_", " ").replace("=", "")
worte = text.split()

wort_anzahl = Counter(worte)
while True:
    try:
        kompakt = input("Wollen sie eine kompakte Ausgabe? [j/N]: ").lower()
        if kompakt == "j":
            kompakte_ausgabe(wort_anzahl)
            break

        elif kompakt == "n":
            ausführliche_ausgabe(wort_anzahl)
            break

        else:
            raise ValueError

    except ValueError:
        print("Bitte gib j oder n ein.")