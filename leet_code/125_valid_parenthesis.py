# https://leetcode.com/problems/valid-parentheses

from typing import List
import unittest

# Runtime: 32 ms, faster than 75.89% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 44.3 MB, less than 7.41 % of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = self.process_stack([], s)

        return len(stack) == 0

    def process_stack(self, stack: List[str], s: str) -> List[str]:
        if len(s) < 1:
            return stack
        elif len(stack) < 1:
            stack.append(s[0])
        elif s[0] == ')' and stack[-1] == '(':
            stack.pop()
        elif s[0] == ']' and stack[-1] == '[':
            stack.pop()
        elif s[0] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(s[0])

        return self.process_stack(stack, s[1:])


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in parenthesis.values():
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char in parenthesis.keys() and stack.pop() != parenthesis[char]:
                return False

        return stack == []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.isValid('()'), True)
        self.assertEqual(self.solution2.isValid('()'), True)

    def test_2(self):
        self.assertEqual(self.solution.isValid('()[]{}'), True)
        self.assertEqual(self.solution2.isValid('()[]{}'), True)

    def test_3(self):
        self.assertEqual(self.solution.isValid('(]'), False)
        self.assertEqual(self.solution2.isValid('(]'), False)

    def test_4(self):
        self.assertEqual(self.solution.isValid('({[]})'), True)
        self.assertEqual(self.solution2.isValid('({[]})'), True)

    def test_5(self):
        self.assertEqual(self.solution.isValid(']'), False)
        self.assertEqual(self.solution2.isValid(']'), False)

    def test_6(self):
        self.assertEqual(self.solution.isValid('(])'), False)
        self.assertEqual(self.solution2.isValid('(])'), False)

    def test_7(self):
        self.assertEqual(self.solution.isValid('){'), False)
        self.assertEqual(self.solution2.isValid('){'), False)

if __name__ == "__main__":
    unittest.main()
