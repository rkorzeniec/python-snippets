# Given two strings, write a method to decide if one is a permutation of the other.

import unittest

class Solution:
    def check(self, s: str, t: str) -> str:
        additional_chars: dict[str, bool] = {}

        for char in s:
            additional_chars[char] = True

        for char in t:
            if char not in additional_chars:
                return False

        return True


class Solution2:
    def check(self, s: str, t: str) -> str:
        additional_chars: str = ''
        left: int = 0
        right: int = len(t) - 1

        while left < right:
            if t[left] not in s:
                additional_chars += t[left]

            if t[right] not in s:
                additional_chars += t[right]

            left += 1
            right -= 1

        return len(additional_chars) < 1


class Solution3:
    def check(self, s: str, t: str) -> str:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        self.assertEqual(self.solution.check('foobar', 'barfoot'), False)
        self.assertEqual(self.solution2.check('foobar', 'barfoot'), False)
        self.assertEqual(self.solution3.check('foobar', 'barfoot'), False)

    def test_2(self):
        self.assertEqual(self.solution.check('ide', 'idea'), False)
        self.assertEqual(self.solution2.check('ide', 'idea'), False)
        self.assertEqual(self.solution3.check('ide', 'idea'), False)

    def test_3(self):
        self.assertEqual(self.solution.check('coding', 'ingcod'), True)
        self.assertEqual(self.solution2.check('coding', 'ingcod'), True)
        self.assertEqual(self.solution3.check('coding', 'ingcod'), True)


if __name__ == "__main__":
    unittest.main()
