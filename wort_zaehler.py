from collections import Counter

def process_text_and_count_words(text_content):
    """
    Processes text content by converting to lowercase, removing punctuation,
    replacing certain characters, splitting into words, and counting word frequencies.
    Returns a Counter object.
    """
    processed_text = text_content.lower()
    # Original line:
    # text = text.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(")", "").replace("(", "").replace(":", "").replace(";", "").replace("„", "").replace("“", "").replace("_", " ").replace("=", "")
    punctuation_to_remove = [".", ",", "!", "?", ")", "(", ":", ";", "„", "“"]
    for punc in punctuation_to_remove:
        processed_text = processed_text.replace(punc, "")
    
    processed_text = processed_text.replace("_", " ").replace("=", "") # Remove "=" by replacing with empty string
    
    words = processed_text.split()
    word_counts = Counter(words)
    return word_counts

def ausführliche_ausgabe(wort_anzahl):
    # For Python 3.7+ Counters remember insertion order.
    # If items are added in a specific order, that order will be preserved.
    # The split() and Counter creation might lead to a specific order.
    # For testing, it's safer to check for presence of calls rather than exact order if not guaranteed.
    for wort, anzahl in wort_anzahl.items():
        print(f"'{wort}' kommt {anzahl}-mal im Text vor.")

def kompakte_ausgabe(wort_anzahl):
    for wort, anzahl in wort_anzahl.items():
        print(f"{wort}: {anzahl}")

if __name__ == "__main__":
    text_input_source = input("Geben Sie einen Text ein oder q wenn Sie einen Dateinamen eingeben wollen: ")
    
    final_text_content = "" # Initialize to ensure it has a value, e.g. if file reading fails
    if text_input_source.lower() == "q":
        while True: # Loop for robust file input
            try:
                dateiname = input("Geben Sie den Dateinamen ein: ")
                # Attempt to open with utf-8, common for text files
                with open(dateiname, "r", encoding="utf-8") as datei:
                    final_text_content = datei.read()
                break 
            except FileNotFoundError:
                print(f"Datei '{dateiname}' nicht gefunden. Bitte versuchen Sie es erneut.")
            except UnicodeDecodeError: # Handle cases where file is not utf-8
                print(f"Datei '{dateiname}' konnte nicht mit UTF-8 gelesen werden. Versuche System-Standardkodierung...")
                try:
                    with open(dateiname, "r") as datei: # Fallback to system default encoding
                        final_text_content = datei.read()
                    break
                except Exception as e_fallback:
                    print(f"Konnte Datei auch mit Standardkodierung nicht lesen: {e_fallback}")
                    final_text_content = None # Indicate error clearly
                    break
            except Exception as e: # Catch other potential file errors
                print(f"Ein Fehler ist aufgetreten beim Lesen der Datei: {e}")
                final_text_content = None # Indicate error clearly
                break 
    else:
        final_text_content = text_input_source

    if final_text_content is not None: # Proceed only if text content is available
        wort_anzahl_ergebnis = process_text_and_count_words(final_text_content)

        # Original logic for choosing output:
        while True:
            try:
                kompakt_wahl = input("Wollen sie eine kompakte Ausgabe? [j/N]: ").lower()
                if kompakt_wahl == "j":
                    kompakte_ausgabe(wort_anzahl_ergebnis)
                    break
                elif kompakt_wahl == "n" or kompakt_wahl == "": # Default to 'n' (ausführlich) if empty
                    ausführliche_ausgabe(wort_anzahl_ergebnis)
                    break
                else:
                    # No explicit raise ValueError, just re-prompt for clarity
                    print("Ungültige Eingabe. Bitte geben Sie 'j' für Ja oder 'n' für Nein ein (oder Enter für ausführlich).")
            except Exception as e_output: # Catch potential errors during output choice/process
                print(f"Ein Fehler ist aufgetreten bei der Ausgabe: {e_output}")
                break
    else:
        print("Kein Text zum Verarbeiten vorhanden.")
