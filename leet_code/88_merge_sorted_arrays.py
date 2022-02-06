# https://leetcode.com/problems/merge-sorted-array/

from typing import List
import unittest

# Runtime: 60 ms, faster than 28.30% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.8 MB, less than 98.42 % of Python3 online submissions for Merge Sorted Array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        nums1[:n] = nums2[:n]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    def test_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        self.assertEqual(self.service.merge(nums1, 3, [2, 5, 6], 3), None)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_2(self):
        nums1 = [1]
        self.assertEqual(self.service.merge(nums1, 1, [], 0), None)
        self.assertEqual(nums1, [1])

    def test_3(self):
        nums1 = [0]
        self.assertEqual(self.service.merge(nums1, 0, [1], 1), None)
        self.assertEqual(nums1, [1])

    def test_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        self.assertEqual(self.service.merge(nums1, 3, [1, 2, 3], 3), None)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_5(self):
        nums1 = [1, 2, 4, 5, 6, 0]
        self.assertEqual(self.service.merge(nums1, 5, [3], 1), None)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
