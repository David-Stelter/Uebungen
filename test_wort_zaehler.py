import unittest
from unittest.mock import patch, call
from collections import Counter
# Ensure this import matches the refactored filename if it was changed.
# The subtask implies wort_zaehler.py is the correct, refactored ASCII-named file.
from wort_zaehler import process_text_and_count_words, ausführliche_ausgabe, kompakte_ausgabe

class TestWortZaehlerLogic(unittest.TestCase):

    # Tests for process_text_and_count_words
    def test_simple_text(self):
        self.assertEqual(process_text_and_count_words("Hallo Welt Hallo"), Counter({'hallo': 2, 'welt': 1}))

    def test_text_with_punctuation(self):
        self.assertEqual(process_text_and_count_words("Hallo, Welt! Hallo."), Counter({'hallo': 2, 'welt': 1}))

    def test_text_with_mixed_case(self):
        self.assertEqual(process_text_and_count_words("Hallo Welt hallo"), Counter({'hallo': 2, 'welt': 1}))

    def test_text_with_underscore_and_equals(self):
        # "Wort_eins Wort=zwei" -> lower: "wort_eins wort=zwei"
        # -> replace "_": "wort eins wort=zwei"
        # -> replace "=": "wort eins wortzwei"
        # -> split: ['wort', 'eins', 'wortzwei']
        self.assertEqual(process_text_and_count_words("Wort_eins Wort=zwei"), Counter({'wort': 1, 'eins': 1, 'wortzwei': 1}))

    def test_empty_text(self):
        self.assertEqual(process_text_and_count_words(""), Counter())

    def test_text_with_only_punctuation(self):
        self.assertEqual(process_text_and_count_words(".,!?"), Counter())
        self.assertEqual(process_text_and_count_words("„“():;"), Counter())

    def test_text_with_german_characters_and_punctuation(self):
        # Ensure äöüß are handled correctly (they should be, as they are part of words)
        self.assertEqual(process_text_and_count_words("schöne grüße, süßer!"), Counter({'schöne': 1, 'grüße': 1, 'süßer':1}))

    # Tests for ausführliche_ausgabe
    @patch('builtins.print')
    def test_ausfuehrliche_ausgabe(self, mock_print):
        sample_counter = Counter({'test': 2, 'wort': 1})
        # Note: Counter items order is deterministic for Python 3.7+ based on insertion.
        # If the Counter is created as Counter(['test', 'test', 'wort']), order is 'test', 'wort'.
        # If Counter({'test':2, 'wort':1}), order might depend on dict's internal order before 3.7,
        # but for 3.7+ it's insertion order of keys. Let's assume 'test' then 'wort'.
        # To be robust against order changes, we can check for any_call or sort calls.
        ausführliche_ausgabe(sample_counter)
        
        expected_calls = [
            call("'test' kommt 2-mal im Text vor."),
            call("'wort' kommt 1-mal im Text vor.")
        ]
        # Check if all expected calls are present, regardless of order.
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)
        self.assertEqual(mock_print.call_count, len(expected_calls))


    # Tests for kompakte_ausgabe
    @patch('builtins.print')
    def test_kompakte_ausgabe(self, mock_print):
        sample_counter = Counter({'test': 2, 'wort': 1})
        # Same order consideration as above.
        kompakte_ausgabe(sample_counter)
        
        expected_calls = [
            call("test: 2"),
            call("wort: 1")
        ]
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)
        self.assertEqual(mock_print.call_count, len(expected_calls))

    @patch('builtins.print')
    def test_ausfuehrliche_ausgabe_empty_counter(self, mock_print):
        sample_counter = Counter()
        ausführliche_ausgabe(sample_counter)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_kompakte_ausgabe_empty_counter(self, mock_print):
        sample_counter = Counter()
        kompakte_ausgabe(sample_counter)
        mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
