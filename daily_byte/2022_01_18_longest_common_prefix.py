import unittest

class LongestCommonPrefix:
    def find(self, words: str) -> str:
        result: str = ''
        shortest_word = min(words)

        for index in range(len(shortest_word)):
            for word in words[1:]:
                if word[index] != shortest_word[index]:
                    return result

            result += shortest_word[index]

        return result

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.service = LongestCommonPrefix()

    def test_1(self):
        self.assertEqual(self.service.find(
            ["colorado", "color", "cold"]), 'col'
        )

    def test_2(self):
        self.assertEqual(self.service.find(["a", "b", "c"]), '')

    def test_3(self):
        self.assertEqual(self.service.find(["spot", "spotty", "spotted"]), 'spot')

if __name__ == "__main__":
    unittest.main()
