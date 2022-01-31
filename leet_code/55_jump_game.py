# https://leetcode.com/problems/jump-game/

from typing import List
import unittest

# Runtime: 760 ms, faster than 36.28% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 36.99 % of Python3 online submissions for Jump Game.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_length: int = len(nums) - 1
        index: int = 0
        max_index: int = 0

        while index < nums_length:
            if index > max_index:
                return False

            max_index = max(max_index, index + nums[index])
            index += 1

        return max_index >= nums_length


# Runtime: 520 ms, faster than 63.41% of Python3 online submissions for Jump Game.
# Memory Usage: 15.1 MB, less than 91.50 % of Python3 online submissions for Jump Game.
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        max_index: int = 0

        for index, num in enumerate(nums):
            if index > max_index:
                return False

            max_index = max(max_index, index + num)

        return True



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()
        self.service2 = Solution2()

    def test_1(self):
        self.assertEqual(self.service.canJump([2, 3, 1, 1, 4]), True)
        self.assertEqual(self.service2.canJump([2, 3, 1, 1, 4]), True)

    def test_2(self):
        self.assertEqual(self.service.canJump([3, 2, 1, 0, 4]), False)
        self.assertEqual(self.service2.canJump([3, 2, 1, 0, 4]), False)

    def test_3(self):
        self.assertEqual(self.service.canJump([2, 0, 0]), True)
        self.assertEqual(self.service2.canJump([2, 0, 0]), True)

    def test_4(self):
        self.assertEqual(self.service.canJump([2, 5, 0, 0]), True)
        self.assertEqual(self.service2.canJump([2, 5, 0, 0]), True)

    def test_5(self):
        self.assertEqual(self.service.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]), True)
        self.assertEqual(self.service2.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]), True)

    def test_6(self):
        self.assertEqual(self.service.canJump([0, 2, 3]), False)
        self.assertEqual(self.service2.canJump([0, 2, 3]), False)

if __name__ == "__main__":
    unittest.main()
