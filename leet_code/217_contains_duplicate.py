# https://leetcode.com/problems/contains-duplicate/

from typing import List, Optional
import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_nums: dict[int, int] = {}

        for num in nums:
            if num in check_nums:
                return True
            check_nums[num] = num

        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(self.solution2.containsDuplicate([1, 2, 3, 1]), True)

    def test_2(self):
        self.assertEqual(self.solution.containsDuplicate([1, 2, 3, 4]), False)
        self.assertEqual(self.solution2.containsDuplicate([1, 2, 3, 4]), False)

    def test_3(self):
        self.assertEqual(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
        self.assertEqual(self.solution2.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

    def test_4(self):
        self.assertEqual(self.solution.containsDuplicate([1000000000,1000000000,11]), True)
        self.assertEqual(self.solution2.containsDuplicate([1000000000,1000000000,11]), True)

    def test_5(self):
        self.assertEqual(self.solution.containsDuplicate([0]), False)
        self.assertEqual(self.solution2.containsDuplicate([0]), False)

    def test_6(self):
        self.assertEqual(self.solution.containsDuplicate([1,5,-2,-4,0]), False)
        self.assertEqual(self.solution2.containsDuplicate([1,5,-2,-4,0]), False)


if __name__ == "__main__":
    unittest.main()
