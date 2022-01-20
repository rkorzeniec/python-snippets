# https://leetcode.com/problems/valid-palindrome/

import re
from typing import List
import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]+", '', s.lower())

        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]+", '', s.lower())
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.isPalindrome(' '), True)
        self.assertEqual(self.solution2.isPalindrome(' '), True)

    def test_2(self):
        self.assertEqual(self.solution.isPalindrome('A man, a plan, a canal: Panama.'), True)
        self.assertEqual(self.solution2.isPalindrome('A man, a plan, a canal: Panama.'), True)

    def test_3(self):
        self.assertEqual(self.solution.isPalindrome('race a car'), False)
        self.assertEqual(self.solution2.isPalindrome('race a car'), False)

    def test_4(self):
        self.assertEqual(self.solution.isPalindrome('ab_a'), True)
        self.assertEqual(self.solution2.isPalindrome('ab_a'), True)

if __name__ == "__main__":
    unittest.main()
