import random
import time
worte = ("Apfel", "Mensch", "Banane", "Schule", "Spass", "Haus", "Computer", "Programmieren", "Python", "Buch", "Tisch", "Stuhl", "Lampe", "Fenster", "Tuer", "Auto", "Strasse", "Himmel", "Wolke", "Sonne", "Mond", "Sterne", "Wasser", "Feuer", "Erde", "Luft", "Pflanze", "Tier", "Mensch", "Kopf", "Auge", "Nase", "Mund", "Ohr", "Hand", "Fuss", "Bein", "Arm", "Bauch", "Ruecken", "Herz", "Leber", "Niere", "Lunge", "Magen", "Darm", "Blut", "Knochen", "Muskel", "Haut", "Haar", "Zahn", "Zunge", "Finger", "Zeh", "Nagel", "Knie", "Ellbogen", "Schulter", "Hals", "Brust", "Ruecken", "Po", "Schwanz", "Fluegel", "Schnabel", "Feder", "Kralle", "Zaun", "Tor", "Wiese", "Feld", "Berg", "Tal", "Fluss", "See", "Meer", "Ozean", "Insel", "Kontinent", "Land", "Staat", "Stadt", "Dorf", "Hauptstadt", "Grenze", "Krieg", "Frieden", "Freiheit", "Gleichheit", "Bruederlichkeit", "Demokratie", "Diktatur", "Monarchie", "Republik", "Sozialismus", "Kapitalismus", "Kommunismus", "Faschismus", "Nationalsozialismus", "Kolonialismus", "Imperialismus", "Globalisierung", "Klimawandel", "Umweltschutz", "Nachhaltigkeit", "Energie", "Strom", "Waerme", "Kaelte", "Licht", "Schatten", "Farbe", "Ton", "Musik", "Kunst", "Malerei", "Bildhauerei", "Architektur", "Literatur", "Dichtung", "Prosa", "Lyrik", "Roman", "Gedicht", "Schrift", "Buchstabe", "Wort", "Satz", "Text", "Sprache", "Grammatik", "Rechtschreibung", "Zeichensetzung", "uebersetzung", "Dolmetschen", "Vokabel", "Woerterbuch", "Lexikon", "Enzyklopaedie", "Bibliothek", "Buchhandlung", "Verlag", "Autor", "Schriftsteller", "Dichter", "Leser", "Bibliothekar", "Buchhaendler", "Verleger", "Drucker", "Buchdrucker", "Buchbinder", "Buchillustrator", "Buchkritiker", "Buchmesse", "Buchpreis")

def wort_waehlen():
    return random.choice(worte)

def eingabe(prompt, eingegebene_buchstaben):
    print("Bereits eingegebene Buchstaben: ", end="")
    for buchstabe in eingegebene_buchstaben:
        print(buchstabe, end=" ")
    buchstabe_raten = input(prompt)
    buchstabe_raten = buchstabe_raten.strip()
    if buchstabe_raten not in eingegebene_buchstaben:
        eingegebene_buchstaben.append(buchstabe_raten)
        return buchstabe_raten.lower(), eingegebene_buchstaben
    else:
        print("Diesen Buchstaben haben Sie bereits geraten.")
        return eingabe(prompt, eingegebene_buchstaben)

def spiel():
    wort = wort_waehlen()
    buchstaben_klein = list(wort.lower())
    buchstaben_normal = list(wort)
    buchstaben_verdeckt = ["_" for _ in buchstaben_normal]
    eingegebene_buchstaben = []
    fehler = 0
    max_fehler = 6
    print("In diesem Spiel gibt es kein ß, ä, ö oder ü. Diese wurden durch ss, ae, oe und ue ersetzt.")
    while fehler < max_fehler and "_" in buchstaben_verdeckt:
        print("".join(buchstaben_verdeckt))
        buchstabe, eingegebene_buchstaben = eingabe("\nGeben Sie einen Buchstaben ein: ", eingegebene_buchstaben)
        if buchstabe in buchstaben_klein:
            for i in range(len(buchstaben_klein)):
                if buchstaben_klein[i] == buchstabe:
                    buchstaben_verdeckt[i] = buchstaben_normal[i]
        else:
            fehler += 1
            print(f"Falsch geraten! Noch {max_fehler - fehler} Versuche uebrig.")
            time.sleep(1)
    
    if "_" not in buchstaben_verdeckt:
        print(f"Herzlichen Glueckwunsch! Sie haben das Wort {wort} erraten.")
    else:
        print(f"Leider verloren! Das Wort war:", wort)

spiel()