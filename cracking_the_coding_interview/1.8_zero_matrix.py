# Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?

from typing import List
import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> bool:
        rows: set[int] = set()
        columns: set[int] = set()

        for row_index, row in enumerate(matrix):
            for column_index, value in enumerate(row):
                if value == 0:
                    rows.add(row_index)
                    columns.add(column_index)

        for row in rows:
            for index in range(len(matrix[row])):
                matrix[row][index] = 0

        for column in columns:
            for index in range(len(matrix)):
                matrix[index][column] = 0

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        matrix = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        exp_matrix = [[0, 0, 0, 0], [5, 6, 0, 0], [9, 10, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(self.solution.rotate(matrix), True)
        self.assertEqual(matrix, exp_matrix)


if __name__ == "__main__":
    unittest.main()
