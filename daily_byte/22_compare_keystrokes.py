# This question is asked by Amazon.
# Given two strings s and t, which represents a sequence of keystrokes,
# where # denotes a backspace,
# return whether or not the sequences produce the same result.
#
# Ex: Given the following strings...
#
# s = "ABC#", t = "CD##AB", return true
# s = "como#pur#ter", t = "computer", return true
# s = "cof#dim#ng", t = "code", return false

from typing import List
import unittest

class Solution:
    def keystrokes(self, s: str, t: str) -> bool:
        s_stack: List[str] = self.build_stack(s)
        t_stack: List[str] = self.build_stack(t)

        return s_stack == t_stack

    def build_stack(self, keystrokes: str) -> List[str]:
        stack: List[str] = []

        for char in keystrokes:
            if char == '#':
                stack.pop()
            else:
                stack.append(char)

        return stack

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.keystrokes('ABC#', 'CD##AB'), True)

    def test_2(self):
        self.assertEqual(self.solution.keystrokes('como#pur#ter', 'computer'), True)

    def test_3(self):
        self.assertEqual(self.solution.keystrokes('cof#dim#ng', 'code'), False)

if __name__ == "__main__":
    unittest.main()
