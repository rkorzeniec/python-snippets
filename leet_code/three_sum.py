# https://leetcode.com/problems/3sum/

from typing import List
import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        triplets: List[List[int]] = []
        previous_num: int = None
        nums = sorted(nums)

        nums.sort()

        for index in range(len(nums) - 2):
            if nums[index] > 0:
                continue
            elif nums[index] == previous_num:
                continue
            else:
                previous_num = nums[index]

            left: int = index + 1
            right: int = len(nums) - 1

            while left < right:
                triplets_sum = nums[index] + nums[left] + nums[right]

                if triplets_sum > 0:
                    right -= 1
                elif triplets_sum < 0:
                    left += 1
                else:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    def test_1(self):
        self.assertEqual(self.service.threeSum(
            [-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )

    def test_2(self):
        self.assertEqual(self.service.threeSum([]), [])

    def test_3(self):
        self.assertEqual(self.service.threeSum([0]), [])

    def test_4(self):
        self.assertEqual(self.service.threeSum([0, 0, 0]), [[0, 0, 0]])

if __name__ == "__main__":
    unittest.main()
