# This question is asked by Amazon.
#
# Given two strings representing sentences, return the words that are not common
# to both strings (i.e. the words that only appear in one of the sentences).
#
# You may assume that each sentence is a sequence of words
# (without punctuation) correctly separated using space characters.

from typing import List, Set
import re
import unittest

class Solution:
    def check(self, s1: List[int], s2: List[int]) -> List[int]:
        different_words: List[str] = []
        s1_words: List[str] = s1.split(' ')
        s2_words: List[str] = s2.split(' ')

        for s1_word in s1_words:
            if s1_word not in s2_words and s1_word not in different_words:
                different_words.append(s1_word)

        for s2_word in s2_words:
            if s2_word not in s1_words and s2_word not in different_words:
                different_words.append(s2_word)

        return different_words


class Solution2:
    def check(self, s1: List[int], s2: List[int]) -> List[int]:
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')

        s1_words = set(s1_words)
        s2_words = set(s2_words)

        different_words = (set(s1_words) - set(s2_words)) | (set(s2_words) - set(s1_words))

        return different_words


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.check("the quick", "brown fox"), ["the", "quick", "brown", "fox"])
        self.assertEqual(self.solution2.check("the quick", "brown fox"), set(["the", "quick", "brown", "fox"]))

    def test_2(self):
        self.assertEqual(self.solution.check("the tortoise beat the haire", "the tortoise lost to the haire"), ["beat", "lost", "to"])
        self.assertEqual(self.solution2.check("the tortoise beat the haire", "the tortoise lost to the haire"), set(["beat", "lost", "to"]))

    def test_3(self):
        self.assertEqual(self.solution.check("copper coffee pot", "hot coffee pot"), ["copper", "hot"])
        self.assertEqual(self.solution2.check("copper coffee pot", "hot coffee pot"), set(["copper", "hot"]))

if __name__ == "__main__":
    unittest.main()
