# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

from typing import List, Set
import re
import unittest

class Solution:
    def is_unique(self, text: str) -> bool:
        chars: dict[str, bool] = {}

        for char in text:
            if char in chars:
                return False
            else:
                chars[char] = True

        return True


class Solution2:
    def is_unique(self, text: str) -> bool:
        return len(set(text)) == len(text)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.is_unique("abcd"), True)
        self.assertEqual(self.solution2.is_unique("abcd"), True)

    def test_2(self):
        self.assertEqual(self.solution.is_unique("a"), True)
        self.assertEqual(self.solution2.is_unique("a"),True)

    def test_3(self):
        self.assertEqual(self.solution.is_unique("abcdefghijklmnopqrstuvxyza"), False)
        self.assertEqual(self.solution2.is_unique("abcdefghijklmnopqrstuvxyza"), False)

if __name__ == "__main__":
    unittest.main()
