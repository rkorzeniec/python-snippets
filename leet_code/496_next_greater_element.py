# https://leetcode.com/problems/next-greater-element-i/

from typing import List
import unittest


# Runtime: 71 ms, faster than 54.62 % of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14 MB, less than 98.44 % of Python3 online submissions for Next Greater Element I.
class Solution:
    def greater_elements(self, nums1: List[int], nums2: List[int]) -> str:
        result: dict[int, int] = {}
        stack: List[int] = []

        for num in nums2:
            while stack and num > stack[-1]:
                result[stack.pop()] = num

            stack.append(num)

        return [result.get(n, -1) for n in nums1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.greater_elements([4, 1, 2], [1, 3, 4, 2]),
            [-1, 3, -1]
        )

    def test_2(self):
        self.assertEqual(
            self.solution.greater_elements([2, 4], [1, 2, 3, 4]),
            [3, -1]
        )

if __name__ == "__main__":
    unittest.main()
