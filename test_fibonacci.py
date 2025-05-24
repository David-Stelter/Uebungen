import unittest
from fibonacci import generate_fibonacci

class TestFibonacciGenerator(unittest.TestCase):

    def test_limit_zero(self):
        self.assertListEqual(generate_fibonacci(0), [])

    def test_limit_one(self):
        self.assertListEqual(generate_fibonacci(1), [0])

    def test_limit_two(self):
        self.assertListEqual(generate_fibonacci(2), [0, 1])

    def test_limit_ten(self):
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertListEqual(generate_fibonacci(10), expected_result)

    def test_negative_limit(self):
        self.assertListEqual(generate_fibonacci(-5), [])

if __name__ == '__main__':
    unittest.main()
