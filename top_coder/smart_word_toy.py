# https://community.topcoder.com/stat?c=problem_statement&pm=3935&rd=6532

from typing import List
import unittest


class SmartWordToy:
    def minPresses(self, start: str, finish: str, forbid: List[str]) -> int:

        return -1


class TestSmartWordToy(unittest.TestCase):
    def setUp(self):
        self.tasks = SmartWordToy()

    def test_1(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "zzzz",
                ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z",
                    "z a z z", "z z a z", "z z z a"]
            ),
            8
        )

    def test_2(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "bbbb",
                []
            ),
            4
        )

    def test_3(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "mmnn",
                []
            ),
            50
        )

    def test_4(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "zzzz",
                ["bz a a a", "a bz a a", "a a bz a", "a a a bz"]
            ),
            -1
        )

    def test_5(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "zzzz",
                ["cdefghijklmnopqrstuvwxyz a a a",
                 "a cdefghijklmnopqrstuvwxyz a a",
                 "a a cdefghijklmnopqrstuvwxyz a",
                 "a a a cdefghijklmnopqrstuvwxyz"]
            ),
            6
        )

    def test_6(self):
        self.assertEqual(
            self.tasks.minPresses(
                "aaaa",
                "zzzz",
                ["b b b b"]
            ),
            -1
        )

    def test_7(self):
        self.assertEqual(
            self.tasks.minPresses(
                "zzzz",
                "aaaa",
                ["abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
                 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk"]
            ),
            -1
        )

if __name__ == "__main__":
    unittest.main()
