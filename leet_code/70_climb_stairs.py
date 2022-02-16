# https://leetcode.com/problems/climbing-stairs/

from typing import List
import unittest

# Time Limit Exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)


# Runtime: 41 ms, faster than 46.90% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 88.65 % of Python3 online submissions for Climbing Stairs.
class Solution2:
    def climbStairs(self, n: int, cache = {}) -> int:
        if n <= 2:
            return n

        if n in cache:
            return cache[n]
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            cache[n] = result

            return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_2(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    # def test_3(self):
    #     self.assertEqual(self.solution.climbStairs(38), 63245986)

    def test_4(self):
        self.assertEqual(self.solution2.climbStairs(2), 2)

    def test_5(self):
        self.assertEqual(self.solution2.climbStairs(3), 3)

    def test_6(self):
        self.assertEqual(self.solution2.climbStairs(38), 63245986)

if __name__ == "__main__":
    unittest.main()
