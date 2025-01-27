from collections import Counter
worte = []

text = input("Geben Sie einen Text ein oder q wenn Sie einen Dateinamen eingeben wollen: ")
if text.lower() == "q":
    dateiname = input("Geben Sie den Dateinamen ein: ")
    with open(dateiname, "r") as datei:
        text = datei.read()
        datei.close()
text = text.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(")", "").replace("(", "").replace(":", "").replace(";", "").replace("„", "").replace("“", "").replace("_", " ").replace("=", "")
worte = text.split()

wort_anzahl = Counter(worte)
print(wort_anzahl)