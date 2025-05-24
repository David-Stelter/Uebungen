import unittest
from unittest.mock import patch, call
import Zahlenraten as zr # Import the module itself to set global variables

class TestZahlenratenHelpers(unittest.TestCase):

    # 1. Tests for oberes_limit_bestimmen()
    @patch('builtins.print') # Suppress print during tests
    @patch('builtins.input')
    def test_valid_limit(self, mock_input, mock_print):
        mock_input.return_value = "10"
        self.assertEqual(zr.oberes_limit_bestimmen(), 10)
        mock_input.assert_called_once_with("Bitte geben Sie das obere Limit (>1) ein: ")

    @patch('builtins.print')
    @patch('builtins.input')
    def test_invalid_input_then_valid_limit(self, mock_input, mock_print):
        mock_input.side_effect = ["abc", "0", "100"]
        self.assertEqual(zr.oberes_limit_bestimmen(), 100)
        self.assertEqual(mock_input.call_count, 3)
        expected_print_calls = [
            call("Bitte gib eine Zahl größer als 1 ein."), # For "abc" (ValueError)
            call("Bitte gib eine Zahl größer als 1 ein.")  # For "0" (ValueError because limit <=1)
        ]
        # Check if all expected calls are present in the actual calls
        for expected_call in expected_print_calls:
            self.assertIn(expected_call, mock_print.call_args_list)
        # Check that print was called exactly for the invalid inputs
        self.assertEqual(mock_print.call_count, len(expected_print_calls))


    @patch('builtins.print')
    @patch('builtins.input')
    def test_limit_is_one_then_valid_limit(self, mock_input, mock_print):
        mock_input.side_effect = ["1", "50"]
        self.assertEqual(zr.oberes_limit_bestimmen(), 50)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with("Bitte gib eine Zahl größer als 1 ein.") # For "1"

    # 2. Tests for rng(oberes_limit)
    @patch('random.randint')
    def test_rng_calls_randint_correctly(self, mock_random_randint):
        zr.rng(100)
        mock_random_randint.assert_called_once_with(1, 100)

    @patch('random.randint')
    def test_rng_returns_randint_value(self, mock_random_randint):
        mock_random_randint.return_value = 42
        self.assertEqual(zr.rng(50), 42)
        mock_random_randint.assert_called_once_with(1, 50)

    # 3. Tests for get_user_guess()
    def setUp_guess_tests(self, limit_value=100):
        """Helper to set the global oberes_limit in Zahlenraten module."""
        zr.oberes_limit = limit_value

    @patch('builtins.print') # Suppress print during tests
    @patch('builtins.input')
    def test_valid_guess(self, mock_input, mock_print):
        self.setUp_guess_tests(100)
        mock_input.return_value = "50"
        self.assertEqual(zr.get_user_guess(), 50)
        mock_input.assert_called_once_with("Bitte gib deine Tipp ein: ")
        mock_print.assert_not_called()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_invalid_input_then_valid_guess(self, mock_input, mock_print):
        self.setUp_guess_tests(100)
        mock_input.side_effect = ["abc", "75"]
        self.assertEqual(zr.get_user_guess(), 75)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with("Bitte gib eine Zahl ein.")

    @patch('builtins.print')
    @patch('builtins.input')
    def test_guess_too_low_then_valid(self, mock_input, mock_print):
        self.setUp_guess_tests(100) # oberes_limit is 100
        mock_input.side_effect = ["0", "25"]
        self.assertEqual(zr.get_user_guess(), 25)
        self.assertEqual(mock_input.call_count, 2)
        # The error message uses zr.oberes_limit + 1
        mock_print.assert_called_once_with(f"Bitte gib eine Zahl über 0 und unter {zr.oberes_limit + 1} ein.")

    @patch('builtins.print')
    @patch('builtins.input')
    def test_guess_too_high_then_valid(self, mock_input, mock_print):
        self.setUp_guess_tests(100) # oberes_limit is 100
        mock_input.side_effect = ["101", "90"]
        self.assertEqual(zr.get_user_guess(), 90)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with(f"Bitte gib eine Zahl über 0 und unter {zr.oberes_limit + 1} ein.")

if __name__ == '__main__':
    unittest.main()
