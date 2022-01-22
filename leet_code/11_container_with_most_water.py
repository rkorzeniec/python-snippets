# https://leetcode.com/problems/container-with-most-water/

from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area: int = 0
        left: int = 0
        right: int = len(height) - 1

        while left < right:
            max_area = max(
                max_area,
                (right - left) * min(height[left], height[right])
            )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    def test_1(self):
        self.assertEqual(self.service.maxArea([1, 1]), 1)

    def test_2(self):
        self.assertEqual(
            self.service.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    # def test_1(self):
    #     self.assertEqual(self.service.maxArea('pwwkew'), 3)

    # def test_1(self):
    #     self.assertEqual(self.service.maxArea(' '), 1)

    # def test_1(self):
    #     self.assertEqual(self.service.maxArea('au'), 2)

    # def test_1(self):
    #     self.assertEqual(self.service.maxArea('dvdf'), 3)

    # def test_1(self):
    #     self.assertEqual(self.service.maxArea('aabaab!bb'), 3)

if __name__ == "__main__":
    unittest.main()
