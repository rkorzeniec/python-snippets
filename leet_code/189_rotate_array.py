# https://leetcode.com/problems/rotate-array

from time import process_time_ns
from typing import List
from collections import deque
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        nums_length = len(nums)
        chunk = nums[nums_length-k:]

        del(nums[nums_length-k:])

        for i, n in enumerate(chunk):
            nums.insert(i, n)

        return nums

class Solution2:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        for i in range(k):
            num = nums.pop(-1)
            nums.insert(0, num)

        return nums


class Solution3:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        nums = deque(nums)
        nums.rotate(k)  # equivalent to nums.appendleft(nums.pop())
        nums = list(nums)

        return nums


# Runtime: 204 ms, faster than 96.86% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.5 MB, less than 84.40 % of Python3 online submissions for Rotate Array.
class Solution4:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        if(k > len(nums) - 1):
            k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
        self.solution4 = Solution4()

    def test_1(self):
        self.assertEqual(self.solution.rotate(
            [1, 2, 3, 4, 5, 6, 7], 3),
            [5, 6, 7, 1, 2, 3, 4]
        )
        self.assertEqual(self.solution2.rotate(
            [1, 2, 3, 4, 5, 6, 7], 3),
            [5, 6, 7, 1, 2, 3, 4]
        )
        self.assertEqual(self.solution3.rotate(
            [1, 2, 3, 4, 5, 6, 7], 3),
            [5, 6, 7, 1, 2, 3, 4]
        )
        self.assertEqual(self.solution4.rotate(
            [1, 2, 3, 4, 5, 6, 7], 3),
            [5, 6, 7, 1, 2, 3, 4]
        )

    def test_2(self):
        self.assertEqual(self.solution.rotate(
            [-1, -100, 3, 99], 2),
            [3, 99, -1, -100]
        )
        self.assertEqual(self.solution2.rotate(
            [-1, -100, 3, 99], 2),
            [3, 99, -1, -100]
        )
        self.assertEqual(self.solution3.rotate(
            [-1, -100, 3, 99], 2),
            [3, 99, -1, -100]
        )
        self.assertEqual(self.solution4.rotate(
            [-1, -100, 3, 99], 2),
            [3, 99, -1, -100]
        )

if __name__ == "__main__":
    unittest.main()
