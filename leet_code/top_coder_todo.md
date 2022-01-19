# https://leetcode.com/problems/two-sum/
# O(n^2) => 4000-5000ms
# O(n log n) => < 100ms

from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict: dict[int, int] = {}

        for index, num in enumerate(nums):
            remaining_target = target - num

            if remaining_target in check_dict:
                return [check_dict[remaining_target], index]

            check_dict[num] = index

        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    def test_1(self):
        self.assertEqual(self.service.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(self.service.twoSum([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(self.service.twoSum([3, 3], 6), [0, 1])

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum(' '), 1)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('au'), 2)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('dvdf'), 3)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('aabaab!bb'), 3)

if __name__ == "__main__":
    unittest.main()
