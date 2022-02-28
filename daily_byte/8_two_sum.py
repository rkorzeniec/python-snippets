"""
This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.
Ex: Given the following...
    [1, 3, 8, 2], k = 10, return true (8 + 2)
    [3, 9, 13, 7], k = 8, return false
    [4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""

from typing import List
import unittest

class Solution:
    def two_sum(self, nums: List[int], k: int) -> bool:
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)

        while left < right:
            remaining = k - (nums[left] + nums[right])

            if remaining == 0:
                return True
            if remaining > 0:
                left += 1
            else:
                right -= 1

        return False


class Solution2:
    def two_sum(self, nums: List[int], k: int) -> bool:
        checked_nums: List[int] = []

        for num in nums:
            remaining = k - num

            if remaining in checked_nums:
                return True

            checked_nums.append(num)

        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.two_sum([1, 3, 8, 2], 10), True)
        self.assertEqual(self.solution2.two_sum([1, 3, 8, 2], 10), True)

    def test_2(self):
        self.assertEqual(self.solution.two_sum([3, 9, 13, 7], 8), False)
        self.assertEqual(self.solution2.two_sum([3, 9, 13, 7], 8), False)

    def test_3(self):
        self.assertEqual(self.solution.two_sum([4, 2, 6, 5, 2], 4), True)
        self.assertEqual(self.solution2.two_sum([4, 2, 6, 5, 2], 4), True)

if __name__ == "__main__":
    unittest.main()
