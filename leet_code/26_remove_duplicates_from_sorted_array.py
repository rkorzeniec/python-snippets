# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        scanned_numbers: List[int] = []
        index: int = 0

        while index < len(nums):
            if nums[index] == None:
                return index

            if nums[index] not in scanned_numbers:
                scanned_numbers.append(nums[index])
                index += 1
            else:
                nums[:] = nums[:index] + nums[index+1:] + [None]

        return index


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        left_index  = 1
        for right_index in range(1, len(nums)):
            if nums[right_index] == nums[right_index - 1]:
                continue
            else:
                nums[left_index] = nums[right_index]
                left_index  += 1

        return left_index


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(self.solution2.removeDuplicates([1, 1, 2]), 2)

    def test_2(self):
        self.assertEqual(
            self.solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
            5
        )
        self.assertEqual(
            self.solution2.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
            5
        )

    def test_3(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1]), 1)
        self.assertEqual(self.solution2.removeDuplicates([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
