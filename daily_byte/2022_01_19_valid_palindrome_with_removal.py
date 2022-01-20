# This question is asked by Facebook. Given a string and the ability to delete at most one character,
# return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

import re
import unittest

class ValidPalindromewithRemoval:
    def check(self, s: str) -> str:
        s: str = re.sub("[^a-zA-Z0-9]+", '', s.lower())
        left: int = 0
        right: int = len(s) - 1
        difference_count: int = 0

        while left < right and difference_count < 2:
            if s[left] != s[right]:
                difference_count += 1

            left += 1
            right -= 1

        return difference_count < 2

class TestValidPalindromewithRemoval(unittest.TestCase):
    def setUp(self):
        self.service = ValidPalindromewithRemoval()

    def test_1(self):
        self.assertEqual(self.service.check('abcba'), True)

    def test_2(self):
        self.assertEqual(self.service.check('foobof'), True)

    def test_3(self):
        self.assertEqual(self.service.check('abccab'), False)

if __name__ == "__main__":
    unittest.main()
