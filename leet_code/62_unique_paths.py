# https://leetcode.com/problems/unique-paths/

from typing import List
import unittest
from unittest import result

# Time Limit Exceeded
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


# Runtime: 49 ms, faster than 33.36% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 95.18 % of Python3 online submissions for Unique Paths.
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        results_cache: List[List[int]] = self.build_results_cache(m, n)

        for i in range(m):
            results_cache[i][0] = 1

        for j in range(n):
            results_cache[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                results_cache[i][j] = results_cache[i-1][j] + results_cache[i][j-1]

        return results_cache[m-1][n-1]

    def build_results_cache(self, m: int, n: int) -> List[List[int]]:
        return [[0 for _ in range(n)] for _ in range(m)]


# Runtime: 44 ms, faster than 44.81% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 83.92 % of Python3 online submissions for Unique Paths.
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0

        path: int = 1

        for i in range(n, (m + n - 1)):
            path *= i
            path //= (i - n + 1)

        return path


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_2(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_3(self):
        self.assertEqual(self.solution2.uniquePaths(3, 7), 28)

    def test_4(self):
        self.assertEqual(self.solution2.uniquePaths(3, 2), 3)

    def test_5(self):
        self.assertEqual(self.solution2.uniquePaths(23, 12), 193536720)

    def test_6(self):
        self.assertEqual(self.solution3.uniquePaths(3, 7), 28)

    def test_7(self):
        self.assertEqual(self.solution3.uniquePaths(3, 2), 3)

    def test_8(self):
        self.assertEqual(self.solution3.uniquePaths(23, 12), 193536720)

    def test_9(self):
        self.assertEqual(self.solution3.uniquePaths(1, 0), 0)

    def test_10(self):
        self.assertEqual(self.solution3.uniquePaths(0, 1), 0)


if __name__ == "__main__":
    unittest.main()
