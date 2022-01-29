# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List
import unittest

# Runtime: 62 ms, faster than 31.73% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.4 MB, less than 98.52 % of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        pivot: int = 0

        while left <= right:
            pivot = (right + left) // 2

            if nums[pivot] < nums[0]:
                right = pivot - 1
            else:
                left = pivot + 1

        if nums[0] <= target:
            left = 0
        else:
            right = len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] < target:
                left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                return pivot

        return -1


# Runtime: 70 ms, faster than 20.36% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.2 MB, less than 99.71 % of Python3 online submissions for Search in Rotated Sorted Array.
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        pivot: int = 0

        while left <= right:
            pivot = (right + left) // 2

            if nums[pivot] == target:
                return pivot
            elif nums[left] <= nums[pivot]:
                if target < nums[pivot] and target >= nums[left]:
                    right = pivot  - 1
                else:
                    left = pivot + 1
            else:
                if target > nums[pivot] and target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(self.solution2.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_2(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(self.solution2.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_3(self):
        self.assertEqual(self.solution.search([1], 0), -1)
        self.assertEqual(self.solution2.search([1], 0), -1)

    def test_4(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 1), 5)
        self.assertEqual(self.solution2.search([4, 5, 6, 7, 0, 1, 2], 1), 5)

    def test_5(self):
        self.assertEqual(self.solution.search([0, 1, 2, 3, 4, 5, 6, 7], 6), 6)
        self.assertEqual(self.solution2.search([0, 1, 2, 3, 4, 5, 6, 7], 6), 6)

    def test_6(self):
        self.assertEqual(self.solution.search([1, 3], 3), 1)
        self.assertEqual(self.solution2.search([1, 3], 3), 1)

    def test_7(self):
        self.assertEqual(self.solution.search([3, 1], 1), 1)
        self.assertEqual(self.solution2.search([3, 1], 1), 1)


if __name__ == "__main__":
    unittest.main()
