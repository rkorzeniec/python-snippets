# https://community.topcoder.com/stat?c=problem_statement&pm=2923&rd=5854

from typing import List
import unittest


class TallPeople:
    def getPeople(self, people: List[str]) -> List[int]:
        people = [row.split(' ') for row in people]

        tallest_of_shortest = self.find_tallest_of_shortest(people)
        shortest_of_tallest = self.find_shortest_of_tallest(people)

        return [tallest_of_shortest, shortest_of_tallest]


    def find_tallest_of_shortest(self, people: List[List[str]]) -> int:
        shortest_people: List[int] = [int(min(row)) for row in people]

        return max(shortest_people)

    def find_shortest_of_tallest(self, people: List[List[str]]) -> int:
        columns: int = len(people[0])
        tallest_people: List[int] = [0 for _ in range(0, columns)]

        for column_index in range(0, columns):
            for row in people:
                tallest_people[column_index] = max(
                    tallest_people[column_index], int(row[column_index])
                )

        return min(tallest_people)


class TestTallPeople(unittest.TestCase):
    def setUp(self):
        self.tasks = TallPeople()

    def test_1(self):
        self.assertEqual(
            self.tasks.getPeople(["9 2 3", "4 8 7"]),  [4,  7]
        )

    def test_2(self):
        self.assertEqual(
            self.tasks.getPeople(["1 2", "4 5", "3 6"]),  [4,  4]
        )

    def test_3(self):
        self.assertEqual(
            self.tasks.getPeople(["1 1", "1 1"]),  [1, 1]
        )

if __name__ == "__main__":
    unittest.main()
