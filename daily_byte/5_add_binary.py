"""
This question is asked by Apple.
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0
Ex: Given the following binary strings...
    "100" + "1", return "101"
    "11" + "1", return "100"
    "1" + "0", return  "1"
"""

import unittest

class AddBinary:
    def add(self, s1: str, s2: str) -> str:
        max_len: int = max(len(s1), len(s2))
        result: str = ''
        carry: int = 0

        s1 = s1.zfill(max_len)
        s2 = s2.zfill(max_len)

        for index in range(max_len - 1, -1, -1):
            x = carry

            x += 1 if s1[index] == '1' else 0
            x += 1 if s2[index] == '1' else 0

            result = ('1' if x % 2 == 1 else '0') + result
            carry = 0 if x < 2 else 1

        if carry != 0:
            result = '1' + result

        return result


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.service = AddBinary()

    def test_1(self):
        self.assertEqual(self.service.add('100', '1'), '101')

    def test_2(self):
        self.assertEqual(self.service.add('11', '1'), '100')

    def test_3(self):
        self.assertEqual(self.service.add('1', '0'), '1')

    def test_4(self):
        self.assertEqual(self.service.add('1101', '100'), '10001')

if __name__ == "__main__":
    unittest.main()
