import re
import unittest

class ValidPalindrome:
    def check(self, text: str) -> str:
        text = re.sub("[^a-zA-z]+", '', text.lower())

        return text == text[::-1]


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.service = ValidPalindrome()

    def test_1(self):
        self.assertEqual(self.service.check('level'), True)

    def test_2(self):
        self.assertEqual(self.service.check('algorithm'), False)

    def test_3(self):
        self.assertEqual(self.service.check('A man, a plan, a canal: Panama.'), True)

if __name__ == "__main__":
    unittest.main()
