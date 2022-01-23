# This question is asked by Microsoft.
# Given a string, return the index of its first unique character.
# If a unique character does not exist, return -1.

import unittest

class Solution:
    def check(self, s: str) -> int:
        checked_chars: dict[str, int] = {}
        answer: int = -1

        for index in range(len(s)):
            if s[index] in checked_chars:
                del(checked_chars[s[index]])
            else:
                checked_chars[s[index]] = index

        if len(checked_chars) > 0:
            answer = min(checked_chars.values())

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.check('abcabd'), 2)

    def test_2(self):
        self.assertEqual(self.solution.check('thedailybyte'), 1)

    def test_3(self):
        self.assertEqual(self.solution.check('developer'), 0)

    def test_4(self):
        self.assertEqual(self.solution.check('aa'), -1)

    def test_5(self):
        self.assertEqual(
            self.solution.check('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'),
            25
        )

if __name__ == "__main__":
    unittest.main()
