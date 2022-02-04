# Assume you have a method isSubstring which checks if one word is a substring of another.
#
# Given two strings,
# s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of "erbottlewat").

from cgi import test
from typing import List
import unittest

class Solution:
    def is_rotation(self, s1: str, s2: str) -> bool:
        for index in range(len(s1)):
            test_string: str = f'{s1[index+1:]}{s1[:index+1]}'

            if test_string == s2:
                return True

        return False





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.is_rotation('waterbottle', 'erbottlewat'), True)

    def test_2(self):
        self.assertEqual(self.solution.is_rotation('waterbottle', 'bottlewat'), False)


if __name__ == "__main__":
    unittest.main()
