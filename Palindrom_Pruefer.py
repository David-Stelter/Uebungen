import time
def check_palindrom(wort):
    wort = wort.replace(" ", "")
    return wort.lower() == wort[::-1].lower()

while True:
    aktion = input("Willst du überprüfen, ob ein Wort oder Phrase ein Palindrom ist (p), oder das Programm verlassen (l)?: ")
    if aktion.lower() == "p":
        phrase = input("Bitte gib das Wort oder die Phrase ein, die überprüft werden soll: ")
        if check_palindrom(phrase):
            print(phrase, " ist ein Palindrom.")
            time.sleep(1)
        else:
            print(phrase, "ist kein Palindrom.")
            time.sleep(1)
    elif aktion.lower() == "l":
        break
    else:
        print("Bitte gib p oder l ein.")
        time.sleep(2)