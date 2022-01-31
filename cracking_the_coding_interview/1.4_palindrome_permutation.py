# Given a string, write a function to check if it is a permutation of a palin­drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
#
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

import unittest

class Solution:
    def check(self, s: str) -> bool:
        char_counts = self.char_counts(s)
        return self.check_counts(char_counts)

    def char_counts(self, s: str):
        checked_chars: dict[str, int] = {}

        s = s.replace(' ', '').lower()

        for char in s:
            if char in checked_chars:
                checked_chars[char] += 1
            else:
                checked_chars[char] = 1

        return checked_chars

    def check_counts(self, char_counts):
        odd_char: bool = False

        for value in char_counts.values():
            odd_value = value % 2 == 1
            if odd_value and not odd_char:
                odd_char = True
            elif odd_value:
                return False

        return True


class Solution2:
    def check(self, s: str) -> bool:
        checked_chars: dict[str, int] = {}
        odd_chars_count: int = 0

        s = s.replace(' ', '').lower()

        for char in s:
            if char in checked_chars:
                checked_chars[char] += 1
            else:
                checked_chars[char] = 1

            if checked_chars[char] % 2 == 1:
                odd_chars_count += 1
            else:
                odd_chars_count -= 1

        return odd_chars_count <= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.check('Tact Coa'), True)
        self.assertEqual(self.solution2.check('Tact Coa'), True)

    def test_2(self):
        self.assertEqual(self.solution.check('Tatt Coa'), False)
        self.assertEqual(self.solution2.check('Tatt Coa'), False)


if __name__ == "__main__":
    unittest.main()
