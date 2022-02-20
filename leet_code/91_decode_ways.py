# https://leetcode.com/problems/decode-ways/

from typing import List
import unittest

# Runtime: 48 ms, faster than 44.35 % of Python3 online submissions for Decode Ways.
# Memory Usage: 14 MB, less than 78.17 % of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if s[0] == '0':
            return 0

        cache = self.buildCache(len(s))
        cache[0] = cache[1] = 1

        for i in range(2, len(s) + 1):
            print(s[i-1:i])
            if 1 <= int(s[i-1:i]) <= 9:
                cache[i] += cache[i - 1]
            print(cache[i])

            print(s[i-2:i])
            if 10 <= int(s[i-2:i]) <= 26:
                cache[i] += cache[i - 2]
            print(cache[i])
            print()

        return cache[-1]

    def buildCache(self, length: int) -> List[int]:
        return [0 for x in range(length + 1)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.numDecodings('12'), 2)

    def test_2(self):
        self.assertEqual(self.solution.numDecodings('226'), 3)

    def test_3(self):
        self.assertEqual(self.solution.numDecodings('06'), 0)

    def test_4(self):
        self.assertEqual(self.solution.numDecodings('10'), 1)

    def test_4(self):
        self.assertEqual(self.solution.numDecodings('2101'), 1)


if __name__ == "__main__":
    unittest.main()
