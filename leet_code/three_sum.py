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
        print

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
                triplet = [nums[index], nums[left], nums[right]]
                triplet_sum = sum(triplet)

                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    triplets.append(triplet)
                    right -= 1
                    previous_left_num = nums[left]

                    while left < len(nums) and nums[left] == previous_left_num:
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

if __name__ == "__main__":
    unittest.main()
