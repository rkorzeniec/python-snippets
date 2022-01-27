# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters,and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
#
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

import unittest

class Solution:
    def check(self, s: str) -> str:
        return s.strip().replace(' ', '%20')


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.check('Mr John Smith          ',), 'Mr%20John%20Smith')


if __name__ == "__main__":
    unittest.main()
