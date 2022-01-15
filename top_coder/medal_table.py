# https://community.topcoder.com/stat?c=problem_statement&pm=2922&rd=5855

from operator import itemgetter
from typing import List
import unittest


class MedalTable:
    def generate(self, results: List[str]) -> List[str]:
        medals_scores: dict[str, List[int]] = {}

        for result in results:
            countries = result.split(' ')

            for index, country in enumerate(countries):
                if country not in medals_scores:
                    medals_scores[country] = [0, 0, 0]

                medals_scores[country][index] = medals_scores[country][index] + 1

        return self.generate_medals_table(medals_scores)

    def generate_medals_table(self, medals_scores) -> List[str]:
        medals_table: List[str] = []

        for score in self.sort_medals_scores(medals_scores):
            medals_table.append(f'{score[0]} {score[1]} {score[2]} {score[3]}')

        return medals_table

    def sort_medals_scores(self, medals_scores):
        scores = [(k, v[0], v[1], v[2]) for k, v in medals_scores.items()]
        scores_sorted_by_country_name = sorted(scores, key=itemgetter(0))

        return sorted(scores_sorted_by_country_name, key=itemgetter(1, 2, 3), reverse=True)


class TestMedalTable(unittest.TestCase):
    def setUp(self):
        self.tasks = MedalTable()

    def test_1(self):
        self.assertEqual(
            self.tasks.generate(["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"]),
            [
                "KOR 3 1 0",
                "ITA 1 0 0",
                "TPE 0 1 1",
                "CHN 0 1 0",
                "JPN 0 1 0",
                "AUS 0 0 1",
                "GBR 0 0 1",
                "UKR 0 0 1"
            ]
        )

    def test_2(self):
        self.assertEqual(
            self.tasks.generate(["USA AUT ROM"]),["USA 1 0 0",  "AUT 0 1 0",  "ROM 0 0 1"])

    def test_3(self):
        self.assertEqual(
            self.tasks.generate(["GER AUT SUI", "AUT SUI GER", "SUI GER AUT"]),
            ["AUT 1 1 1",  "GER 1 1 1",  "SUI 1 1 1"]
        )

if __name__ == "__main__":
    unittest.main()
