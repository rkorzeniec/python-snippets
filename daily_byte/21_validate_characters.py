# This question is asked by Google.
# Given a string only containing the following characters (, ), {, }, [, and ]
# return whether or not the opening and closing characters are in a valid order.
#
# "(){}[]", return true
# "(({[]}))", return true
# "{(})", return false

from typing import List
import unittest

class Solution:
    def valid(self, characters: str) -> bool:
        stack: List[str] = []
        parenthesis: dict[str, str] = {')': '(', ']': '[', '}': '{'}

        for char in characters:
            if char in parenthesis.values():
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char in parenthesis.keys() and stack.pop() != parenthesis[char]:
                return False

        return len(stack) == 0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.valid('(){}[]'), True)

    def test_2(self):
        self.assertEqual(self.solution.valid('(({[]}))'), True)

    def test_3(self):
        self.assertEqual(self.solution.valid('{(})'), False)

if __name__ == "__main__":
    unittest.main()
