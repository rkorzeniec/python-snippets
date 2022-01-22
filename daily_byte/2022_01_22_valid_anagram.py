# This question is asked by Facebook.
# Given two strings s and t, return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

from typing import List
import unittest

class Solution:
    def valid(self, s: str, t: str) -> int:
        for index in range(len(s)):
            if s[index] not in t:
                return False
            elif s[index] in t:
                t = t.replace(s[index], '')

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.valid('cat', 'tac'), True)

    def test_2(self):
        self.assertEqual(self.solution.valid('listen', 'silent'), True)

    def test_3(self):
        self.assertEqual(self.solution.valid('program', 'function'), False)

    def test_4(self):
        self.assertEqual(self.solution.valid('caat', 'tac'), False)

if __name__ == "__main__":
    unittest.main()
