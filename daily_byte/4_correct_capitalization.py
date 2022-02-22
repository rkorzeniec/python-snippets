import re
import unittest

class CorrectCapitalization:
    def check(self, text: str) -> bool:
        if re.fullmatch('\A[A-Z]+', text) or re.fullmatch('\A[a-zA-Z].[a-z]+\Z', text):
            return True

        return False


class TestCorrectCapitalization(unittest.TestCase):
    def setUp(self):
        self.service = CorrectCapitalization()

    def test_1(self):
        self.assertEqual(self.service.check('USA'), True)

    def test_2(self):
        self.assertEqual(self.service.check('Calvin'), True)

    def test_3(self):
        self.assertEqual(self.service.check('compUter'), False)

    def test_4(self):
        self.assertEqual(self.service.check('coding'), True)

    def test_5(self):
        self.assertEqual(self.service.check('SoftWare'), False)

if __name__ == "__main__":
    unittest.main()
