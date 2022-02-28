"""
This question is asked by Amazon.
Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position.

The string will only contain L, R, U, and D characters,
representing left, right, up, and down respectively.

Ex: Given the following strings...
    "LR", return true
    "URURD", return false
    "RUULLDRD", return true
"""

from typing import List
import unittest

class VacuumCleanerRoute:
    def check(self, text: str) -> bool:
        coordinates: List[int] = [0, 0]

        for action in text:
            if action == 'L':
                coordinates[0] -= 1
            elif action == 'R':
                coordinates[0] += 1
            elif action == 'D':
                coordinates[1] -= 1
            elif action == 'U':
                coordinates[1] += 1

        return coordinates == [0, 0]


class TestVacuumCleanerRoute(unittest.TestCase):
    def setUp(self):
        self.service = VacuumCleanerRoute()

    def test_1(self):
        self.assertEqual(self.service.check('LR'), True)

    def test_2(self):
        self.assertEqual(self.service.check('URURD'), False)

    def test_3(self):
        self.assertEqual(self.service.check('RUULLDRD'), True)

if __name__ == "__main__":
    unittest.main()
