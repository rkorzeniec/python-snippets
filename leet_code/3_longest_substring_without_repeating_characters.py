# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import List
import unittest

# Runtime: 105 ms, faster than 35.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.5 MB, less than 24.73 % of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        scanned_chars: List[str] = []
        result: int = 0

        if len(s) <= 1:
            return len(s)

        for char in s:
            if char in scanned_chars:
                scanned_chars = scanned_chars[scanned_chars.index(char) + 1:]

            scanned_chars.append(char)
            result = max(result, len(scanned_chars))

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    def test_abcabcbb(self):
        self.assertEqual(self.service.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_bbbbb(self):
        self.assertEqual(
            self.service.lengthOfLongestSubstring('bbbbb'), 1)

    def test_pwwkew(self):
        self.assertEqual(self.service.lengthOfLongestSubstring('pwwkew'), 3)

    def test_empty(self):
        self.assertEqual(self.service.lengthOfLongestSubstring(' '), 1)

    def test_au(self):
        self.assertEqual(self.service.lengthOfLongestSubstring('au'), 2)

    def test_dvdf(self):
        self.assertEqual(self.service.lengthOfLongestSubstring('dvdf'), 3)

    def test_aabaab(self):
        self.assertEqual(self.service.lengthOfLongestSubstring('aabaab!bb'), 3)

if __name__ == "__main__":
    unittest.main()
