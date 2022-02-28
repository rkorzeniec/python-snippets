# This question is asked by Facebook.
# Given a string s containing only lowercase letters,
# continuously remove adjacent characters that are the same and return the result.

# Ex: Given the following strings...
# s = "abccba", return ""
# s = "foobar", return "fbar"
# s = "abccbefggfe", return "a"

import unittest

class Solution:
    def remove_adjacent(self, s: str) -> str:
        characters: dict[str, int] = self.build_character_occurrences(s)
        result: str = ''

        for char in characters:
            if characters[char] == 1:
                result += char

        return result



    def build_character_occurrences(self, s: str):
        characters: dict[str, int] = {}

        for char in s:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        return characters

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.remove_adjacent('abccba'), '')

    def test_2(self):
        self.assertEqual(self.solution.remove_adjacent('foobar'), 'fbar')

    def test_3(self):
        self.assertEqual(self.solution.remove_adjacent('abccbefggfe'), 'a')

if __name__ == "__main__":
    unittest.main()
