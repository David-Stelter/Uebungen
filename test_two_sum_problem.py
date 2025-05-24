import unittest
from two_sum_problem import find_sum_pairs_for_range

class TestTwoSumProblemSpecific(unittest.TestCase):

    def test_sum_5(self):
        # target_sum = 5, integers = [0, 1, 2, 3, 4]
        # Pairs: (1,4), (2,3)
        self.assertListEqual(find_sum_pairs_for_range(5), [(1, 4), (2, 3)])

    def test_sum_6(self):
        # target_sum = 6, integers = [0, 1, 2, 3, 4, 5]
        # Pairs: (1,5), (2,4)
        self.assertListEqual(find_sum_pairs_for_range(6), [(1, 5), (2, 4)])

    def test_sum_2(self):
        # target_sum = 2, integers = [0, 1]
        # i=0, j=1: integers[0]+integers[1] = 0+1=1 != 2.
        # Expected: []
        self.assertListEqual(find_sum_pairs_for_range(2), [])

    def test_sum_1(self):
        # target_sum = 1, integers = [0]
        # Outer loop i=0. Inner loop range(1,1) is empty.
        # Expected: []
        self.assertListEqual(find_sum_pairs_for_range(1), [])

    def test_sum_0(self):
        # target_sum = 0, integers = []
        # Outer loop range(0) is empty.
        # Expected: []
        self.assertListEqual(find_sum_pairs_for_range(0), [])

    def test_sum_negative(self):
        # target_sum = -5, integers = [] (range(-5) is empty)
        # Expected: []
        self.assertListEqual(find_sum_pairs_for_range(-5), [])
        
    def test_sum_7(self):
        # target_sum = 7, integers = [0, 1, 2, 3, 4, 5, 6]
        # (0,x) no
        # (1,6)
        # (2,5)
        # (3,4)
        self.assertListEqual(find_sum_pairs_for_range(7), [(1, 6), (2, 5), (3, 4)])

if __name__ == '__main__':
    unittest.main()
