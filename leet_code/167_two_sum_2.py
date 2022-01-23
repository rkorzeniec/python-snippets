# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List
import unittest

# Runtime: 93 ms, faster than 35.12% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.6 MB, less than 63.73 % of Python3 online submissions for Two Sum II - Input Array Is Sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            remaining = target - (numbers[left] + numbers[right])

            if remaining == 0:
                return [left + 1, right + 1]
            if remaining > 0:
                left += 1
            else:
                right -= 1


# Runtime: 60 ms, faster than 90.21% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.8 MB, less than 5.03 % of Python3 online submissions for Two Sum II - Input Array Is Sorted.
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checked_numbers: dict[int, int] = {}

        for index in range(len(numbers)):
            remaining = target - numbers[index]

            if remaining in checked_numbers:
                return [checked_numbers[remaining] + 1, index + 1]

            checked_numbers[numbers[index]] = index


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(self.solution2.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_2(self):
        self.assertEqual(self.solution.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(self.solution2.twoSum([2, 3, 4], 6), [1, 3])

    def test_3(self):
        self.assertEqual(self.solution.twoSum([-1, 0], -1), [1, 2])
        self.assertEqual(self.solution2.twoSum([-1, 0], -1), [1, 2])

    def test_4(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(self.solution2.twoSum([2, 7, 11, 15], 9), [1, 2])

if __name__ == "__main__":
    unittest.main()
