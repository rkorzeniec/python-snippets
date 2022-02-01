# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
#
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string. You can assume the string has
# only uppercase and lowercase letters(a - z).

from typing import List
import unittest

class Solution:
    def compress(self, s: str) -> str:
        index: int = 0
        compressed_string: List[str] = []

        while index < len(s):
            char: str = s[index]
            count: int = 1

            while index < len(s) and s[index] == char:
                count += 1
                index += 1

            compressed_string.append(char)
            compressed_string.append(str(count - 1))

        if len(compressed_string) >= len(s):
            return s

        return ''.join(compressed_string)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.compress('aabcccccaaa',), 'a2b1c5a3')

    def test_2(self):
        self.assertEqual(self.solution.compress('aabccaa',), 'aabccaa')

    def test_3(self):
        self.assertEqual(self.solution.compress('aabbccaa',), 'aabbccaa')


if __name__ == "__main__":
    unittest.main()
