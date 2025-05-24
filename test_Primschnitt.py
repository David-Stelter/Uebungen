import unittest
from unittest.mock import patch
from Primschnitt import sieve_of_eratosthenes, get_valid_integer

class TestSieveOfEratosthenes(unittest.TestCase):

    def test_primes_in_range(self):
        self.assertListEqual(sieve_of_eratosthenes(2, 10), [2, 3, 5, 7])

    def test_no_primes_in_range(self):
        self.assertListEqual(sieve_of_eratosthenes(8, 10), [])

    def test_bounds_are_prime(self):
        self.assertListEqual(sieve_of_eratosthenes(2, 3), [2, 3])

    def test_lower_bound_zero_or_one(self):
        self.assertListEqual(sieve_of_eratosthenes(0, 5), [2, 3, 5])
        self.assertListEqual(sieve_of_eratosthenes(1, 5), [2, 3, 5])

    def test_lower_equals_upper_prime(self):
        self.assertListEqual(sieve_of_eratosthenes(5, 5), [5])

    def test_lower_equals_upper_not_prime(self):
        self.assertListEqual(sieve_of_eratosthenes(4, 4), [])

    def test_large_number_as_upper_bound(self):
        self.assertListEqual(sieve_of_eratosthenes(2, 30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_range_is_reversed(self):
        # Based on the code, if lower_bound > upper_bound, the main loop in sieve_of_eratosthenes
        # `for i in range(2, upper_bound + 1)` might not run as expected or run with upper_bound that is small.
        # The is_prime list is initialized up to upper_bound + 1.
        # If upper_bound is small, say 2, and lower_bound is 10,
        # primes.append(i) condition `if i >= lower_bound:` will prevent addition.
        # Let's test the expected outcome is an empty list.
        self.assertListEqual(sieve_of_eratosthenes(10, 2), [])
        self.assertListEqual(sieve_of_eratosthenes(30, 20), [])


class TestGetValidInteger(unittest.TestCase):

    @patch('builtins.input', side_effect=['123'])
    def test_valid_integer_input(self, mock_input):
        self.assertEqual(get_valid_integer("Enter a number: "), 123)
        mock_input.assert_called_once_with("Enter a number: ")

    @patch('builtins.input', side_effect=['abc', '45'])
    @patch('builtins.print') # To suppress "Bitte gib eine ganze Zahl ein."
    def test_invalid_then_valid_integer_input(self, mock_print, mock_input):
        self.assertEqual(get_valid_integer("Enter an integer: "), 45)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with("Bitte gib eine ganze Zahl ein.")

    @patch('builtins.input', side_effect=['-10'])
    def test_valid_negative_integer_input(self, mock_input):
        self.assertEqual(get_valid_integer("Enter a negative number: "), -10)
        mock_input.assert_called_once_with("Enter a negative number: ")

    @patch('builtins.input', side_effect=['0'])
    def test_valid_zero_input(self, mock_input):
        self.assertEqual(get_valid_integer("Enter zero: "), 0)
        mock_input.assert_called_once_with("Enter zero: ")

    # Testing that the prompt is displayed correctly is implicitly covered by mock_input.assert_called_once_with(PROMPT)
    # in the test_valid_integer_input. If a different prompt were used by the function, the assertion would fail.

if __name__ == '__main__':
    unittest.main()
