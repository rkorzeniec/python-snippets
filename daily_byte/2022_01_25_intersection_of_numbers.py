# This question is asked by Google.
# Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

from typing import List, Set
import re
import unittest

class Solution:
    def check(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection: List[int] = []

        for num1 in nums1:
            if num1 in nums2 and num1 not in intersection:
                intersection.append(num1)

        return intersection


class Solution2:
    def check(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection: Set[int] = set()

        for num1 in nums1:
            if num1 in nums2:
                intersection.add(num1)

        return intersection


class Solution3:
    def check(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        self.assertEqual(self.solution.check([2, 4, 4, 2], [2, 4]), [2, 4])
        self.assertEqual(self.solution2.check([2, 4, 4, 2], [2, 4]), set([2, 4]))
        self.assertEqual(self.solution3.check([2, 4, 4, 2], [2, 4]), set([2, 4]))

    def test_2(self):
        self.assertEqual(self.solution.check([1, 2, 3, 3], [3, 3]), [3])
        self.assertEqual(self.solution2.check([1, 2, 3, 3], [3, 3]), set([3]))
        self.assertEqual(self.solution3.check([1, 2, 3, 3], [3, 3]), set([3]))

    def test_3(self):
        self.assertEqual(self.solution.check([2, 4, 6, 8], [1, 3, 5, 7]), [])
        self.assertEqual(self.solution2.check([2, 4, 6, 8], [1, 3, 5, 7]), set())
        self.assertEqual(self.solution3.check([2, 4, 6, 8], [1, 3, 5, 7]), set())

if __name__ == "__main__":
    unittest.main()
