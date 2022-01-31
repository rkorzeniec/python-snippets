# https://leetcode.com/problems/maximum-subarray/

from typing import List
import unittest

# Runtime: 780 ms, faster than 59.73% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.9 MB, less than 97.47 % of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum: int = nums[0]
        current_sum: int = max_sum

        for num in nums[1:]:
            current_sum += num
            current_sum = max(current_sum, num)

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# Runtime: 676 ms, faster than 95.80% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28 MB, less than 94.45 % of Python3 online submissions for Maximum Subarray.
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum: int = nums[0]
        current_sum: int = max_sum

        for num in nums[1:]:
            if current_sum > 0:
                current_sum += num
            else:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()
        self.service2 = Solution2()

    def test_1(self):
        self.assertEqual(self.service.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.service2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_2(self):
        self.assertEqual(self.service.maxSubArray([1]), 1)
        self.assertEqual(self.service2.maxSubArray([1]), 1)

    def test_3(self):
        self.assertEqual(self.service.maxSubArray([5, 4, -1, 7, 8]), 23)
        self.assertEqual(self.service2.maxSubArray([5, 4, -1, 7, 8]), 23)

if __name__ == "__main__":
    unittest.main()
