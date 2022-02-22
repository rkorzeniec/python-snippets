# This question is asked by Amazon. Given a string representing your stones
# and another string representing a list of jewels,
# return the number of stones that you have that are also jewels.

from typing import List
import unittest

class Solution:
    def count(self, jewels: str, stones: str) -> int:
        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1

        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.count('abc', 'ac'), 2)

    def test_2(self):
        self.assertEqual(self.solution.count('Af', 'AaaddfFf'), 3)

    def test_3(self):
        self.assertEqual(self.solution.count('AYOPD', 'ayopd'), 0)

if __name__ == "__main__":
    unittest.main()
