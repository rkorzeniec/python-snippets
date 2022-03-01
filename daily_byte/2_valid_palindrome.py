"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
Ex: Given the following strings...
    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true
"""

import re
import unittest

class ValidPalindrome:
    def check(self, text: str) -> str:
        text = re.sub("[^a-zA-z]+", '', text.lower())

        return text == text[::-1]


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.service = ValidPalindrome()

    def test_1(self):
        self.assertEqual(self.service.check('level'), True)

    def test_2(self):
        self.assertEqual(self.service.check('algorithm'), False)

    def test_3(self):
        self.assertEqual(self.service.check('A man, a plan, a canal: Panama.'), True)

if __name__ == "__main__":
    unittest.main()
