# This question is asked by Amazon.
# Given two arrays of numbers, where the first array is a subset of the second array,
# return an array containing all the next greater elements for each element in the first array, in the second array.
# If there is no greater element for any element, output -1 for that number.

# Ex: Given the following arrays…
# nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
# nums1 = [2, 4], nums2 = [1, 2, 3, 4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.

from typing import List
import unittest

class Solution:
    def greater_elements(self, nums1: List[int], nums2: List[int]) -> str:
        result: dict[int, int] = {}
        stack: List[int] = []

        for num in nums2:
            while stack and num > stack[-1]:
                result[stack.pop()] = num

            stack.append(num)

        return [result.get(n, -1) for n in nums1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.greater_elements([4, 1, 2], [1, 3, 4, 2]),
            [-1, 3, -1]
        )

    def test_2(self):
        self.assertEqual(
            self.solution.greater_elements([2, 4], [1, 2, 3, 4]),
            [3, -1]
        )

if __name__ == "__main__":
    unittest.main()
