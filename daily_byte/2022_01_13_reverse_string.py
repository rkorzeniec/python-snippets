# https://community.topcoder.com/stat?c=problem_statement&pm=1585&rd=6535
import unittest

class ReverseString:
    def reverse(self, text: str) -> str:
        reversed_text: str = ''

        for i in range(len(text)-1, -1, -1):
            reversed_text += text[i]

        return reversed_text

    def reverse2(self, text: str) -> str:
        return text[::-1]


class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.reverser = ReverseString()

    def test_cat(self):
        self.assertEqual(self.reverser.reverse('Cat'), 'taC')

    def test_sentence(self):
        self.assertEqual(
            self.reverser.reverse('The Daily Byte'), 'etyB yliaD ehT'
        )

    def test_civic(self):
        self.assertEqual(self.reverser.reverse('civic'), 'civic')

    def test_cat2(self):
        self.assertEqual(self.reverser.reverse2('Cat'), 'taC')

    def test_sentence2(self):
        self.assertEqual(
            self.reverser.reverse2('The Daily Byte'), 'etyB yliaD ehT'
        )

    def test_civic2(self):
        self.assertEqual(self.reverser.reverse2('civic'), 'civic')

if __name__ == "__main__":
    unittest.main()
