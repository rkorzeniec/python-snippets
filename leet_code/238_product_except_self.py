# https://leetcode.com/problems/product-of-array-except-self

from typing import List, Optional
import unittest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer: List[int] = []

        for i in range(len(nums)):
            product: Optional[int] = None

            for j, num in enumerate(nums):
                if i == j:
                    continue

                if product == None:
                    product = num
                else:
                    product *= num

            answer.append(product)

        return answer


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer: List[int] = [1 for i in nums]

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            answer[i] = product

        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            answer[i] *= product

        return answer


# Runtime: 239 ms, faster than 74.11% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21 MB, less than 93.53 % of Python3 online submissions for Product of Array Except Self.
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros_count = 0

        for n in nums:
            if n == 0:
                zeros_count += 1
            else:
                product *= n

        if zeros_count == 0:
            for i in range(len(nums)):
                nums[i] = int(product / nums[i])

        elif zeros_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0

        else:
            nums = [0] * len(nums)

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4]),
            [24,12,8,6]
        )

        self.assertEqual(
            self.solution2.productExceptSelf([1, 2, 3, 4]),
            [24, 12, 8, 6]
        )

        self.assertEqual(
            self.solution3.productExceptSelf([1, 2, 3, 4]),
            [24, 12, 8, 6]
        )

    def test_2(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0]
        )

        self.assertEqual(
            self.solution2.productExceptSelf([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0]
        )

        self.assertEqual(
            self.solution3.productExceptSelf([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
