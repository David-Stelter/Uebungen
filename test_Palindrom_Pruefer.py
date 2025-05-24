import unittest
from Palindrom_Pruefer import check_palindrom

class TestPalindromPruefer(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(check_palindrom("madam"))
        self.assertTrue(check_palindrom("racecar"))
        self.assertTrue(check_palindrom("level"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(check_palindrom("nurses run"))
        self.assertTrue(check_palindrom("taco cat"))
        self.assertTrue(check_palindrom("my gym"))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(check_palindrom("Madam"))
        self.assertTrue(check_palindrom("RaceCaR"))
        self.assertTrue(check_palindrom("LeVel"))

    def test_non_palindrome(self):
        self.assertFalse(check_palindrom("hello"))
        self.assertFalse(check_palindrom("world"))
        self.assertFalse(check_palindrom("python"))

    def test_empty_string(self):
        self.assertTrue(check_palindrom(""))

    def test_single_character(self):
        self.assertTrue(check_palindrom("a"))
        self.assertTrue(check_palindrom("Z"))
        self.assertTrue(check_palindrom("7"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(check_palindrom("121"))
        self.assertTrue(check_palindrom("A man a plan a canal Panama 121")) # The function seems to handle spaces and case, so this should work.
        self.assertTrue(check_palindrom("Was it a car or a cat I saw 11"))

if __name__ == '__main__':
    unittest.main()
