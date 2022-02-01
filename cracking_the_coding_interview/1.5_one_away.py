# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

#
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

import unittest

class Solution:
    def check(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            return self.check_replace(s1, s2)
        elif len(s1) + 1 == len(s2):
            return self.check_insert(s1, s2)
        elif len(s1) - 1 == len(s2):
            return self.check_insert(s2, s1)

        return False

    def check_replace(self, s1: str, s2: str) -> bool:
        char_replaced: bool = False

        for index in range(len(s1)):
            if s1[index] != s2[index]:
                if char_replaced:
                    return False

                char_replaced = True

        return True

    def check_insert(self, s1: str, s2: str) -> bool:
        index1: int = 0
        index2: int = 0

        while index1 < len(s1) and index2 < len(s2):
            if s1[index1] != s2[index2]:
                if index1 != index2:
                    return False

                index2 += 1
            else:
                index1 += 1
                index2 += 1

        return True


class Solution2():
    def check(self, s1: str, s2: str) -> bool:
        return self.edit_distance(s1, s2, len(s1), len(s2)) <= 1

    def edit_distance(self, s1: str, s2: str, s1_len: int, s2_len: int) -> bool:
        if s1_len == 0:
            return s2_len

        if s2_len == 0:
            return s1_len

        if s1[s1_len-1] == s2[s2_len-1]:
            return self.edit_distance(s1, s2, s1_len-1, s2_len-1)

        return 1 + min(
            self.edit_distance(s1, s2, s1_len, s2_len-1),    # Insert
            self.edit_distance(s1, s2, s1_len-1, s2_len),    # Remove
            self.edit_distance(s1, s2, s1_len-1, s2_len-1)    # Replace
        )





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        self.assertEqual(self.solution.check('pale', 'ple'), True)
        self.assertEqual(self.solution2.check('pale', 'ple'), True)

    def test_2(self):
        self.assertEqual(self.solution.check('pales', 'pale'), True)
        self.assertEqual(self.solution2.check('pales', 'pale'), True)

    def test_3(self):
        self.assertEqual(self.solution.check('pale', 'bale'), True)
        self.assertEqual(self.solution2.check('pale', 'bale'), True)

    def test_4(self):
        self.assertEqual(self.solution.check('pale', 'bake'), False)
        self.assertEqual(self.solution2.check('pale', 'bake'), False)

    def test_5(self):
        self.assertEqual(self.solution.check('pale', 'paless'), False)
        self.assertEqual(self.solution2.check('pale', 'paless'), False)

    def test_6(self):
        self.assertEqual(self.solution.check('pale', 'pa'), False)
        self.assertEqual(self.solution2.check('pale', 'pa'), False)


if __name__ == "__main__":
    unittest.main()
