# https://community.topcoder.com/stat?c=problem_statement&pm=1585&rd=6535

from typing import List
import unittest


class BusinessTasks:
    def getTask(self, tasks: List[str], seed: int) -> str:
        taskIndex = 0

        while len(tasks) > 1:
            for i in range(seed - 1):
                taskIndex = (taskIndex + 1) % len(tasks)

            tasks.remove(tasks[taskIndex])

        return tasks.pop()


class TestBusinessTasks(unittest.TestCase):
    def setUp(self):
        self.tasks = BusinessTasks()

    def test_1(self):
        self.assertEqual(self.tasks.getTask(["a", "b", "c", "d"], 2), 'a')

    def test_2(self):
        self.assertEqual(
            self.tasks.getTask(["a", "b", "c", "d", "e"], 3), 'd')

    def test_3(self):
        self.assertEqual(self.tasks.getTask(
            ["alpha", "beta", "gamma", "delta", "epsilon"], 1), 'epsilon'
        )

    def test_4(self):
        self.assertEqual(self.tasks.getTask(["a", "b"], 1000), 'a')

    def test_5(self):
        self.assertEqual(self.tasks.getTask(
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            17
        ), 'n')

    def test_6(self):
        self.assertEqual(self.tasks.getTask(
            ["zlqamum", "yjsrpybmq", "tjllfea", "fxjqzznvg", "nvhekxr", "am", "skmazcey", "piklp", "olcqvhg", "dnpo",
                "bhcfc", "y", "h", "fj", "bjeoaxglt", "oafduixsz", "kmtbaxu", "qgcxjbfx", "my", "mlhy", "bt", "bo", "q"],
            9000000
        ), 'fxjqzznvg')


if __name__ == "__main__":
    unittest.main()
