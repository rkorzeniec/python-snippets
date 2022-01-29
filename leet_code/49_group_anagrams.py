# https://leetcode.com/problems/group-anagrams/

from typing import List
import unittest

# Runtime: 108 ms, faster than 65.43% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.3 MB, less than 30.61 % of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        checked_strings: dict[str, List[str]] = {}

        for string in strs:
            sorted_string = str(sorted(string))

            if sorted_string in checked_strings:
                checked_strings[sorted_string].append(string)
            else:
                checked_strings[sorted_string] = [string]

        return checked_strings.values()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            list(self.solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])),
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        )

    def test_2(self):
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])

    def test_3(self):
        self.assertEqual(self.solution.groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
