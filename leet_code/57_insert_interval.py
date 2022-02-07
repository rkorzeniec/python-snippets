# https://leetcode.com/problems/insert-interval/

from typing import List
import unittest

# Runtime: 84 ms, faster than 72.03% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.4 MB, less than 64.57 % of Python3 online submissions for Insert Interval.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START: int = 0
        END: int = 1

        left: List[List[int]] = []
        right: List[List[int]] = []

        for interval in intervals:
            if interval[END] < newInterval[START]:
                left.append(interval)
            elif interval[START] > newInterval[END]:
                right.append(interval)
            else:
                newInterval[START] = min(newInterval[START], interval[START])
                newInterval[END] = max(newInterval[END], interval[END])

        return left + [newInterval] + right

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.insert([[1, 3], [6, 9]], [2, 5]),
            [[1, 5], [6, 9]]
        )

    def test_2(self):
        self.assertEqual(
            self.solution.insert(
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8]
            ),
            [[1, 2], [3, 10], [12, 16]]
        )

    def test_3(self):
        self.assertEqual(
            self.solution.insert([[1, 3], [6, 9]], [4, 5]),
            [[1, 3], [4, 5], [6, 9]]
        )


if __name__ == "__main__":
    unittest.main()
