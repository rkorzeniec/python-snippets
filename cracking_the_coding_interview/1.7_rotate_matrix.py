# Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?

from typing import List
import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> bool:
        length: int = len(matrix)

        if length == 0 or length != len(matrix[0]):
            return False

        for row in range(length // 2):
            first:int = row
            last: int = length - 1 - first

            i: int = first
            while i < last:
                offset: int = i - first
                top: int = matrix[first][i]

                # left -> top
                matrix[first][i] = matrix[last-offset][first]

                # bottom -> left
                matrix[last-offset][first] = matrix[last][last-offset]

                # right -> bottom
                matrix[last][last-offset] = matrix[i][last]

                # top -> right
                matrix[i][last] = top

                i += 1

        return True





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        exp_matrix = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

        self.assertEqual(self.solution.rotate(matrix), True)
        self.assertEqual(matrix, exp_matrix)


if __name__ == "__main__":
    unittest.main()
