# This question is asked by Google.
# Given the reference to the root of a binary search tree and a search value,
# return the reference to the node that contains the value if it exists and null otherwise.

# NOTE: all values in the binary search tree will be unique.

# Ex: Given the tree...

#         3
#        / \
#       1   4
# and the search value 1 return a reference to the node containing 1.

# Ex: Given the following tree...
#         7
#        / \
#       5   9
#          / \
#         8   10
# and the search value 9 return a reference to the node containing 9.

# Ex: Given the following tree...
#         8
#        / \
#       6   9
# and the search value 7 return null.

from typing import Optional, Union
import unittest


class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_value(self, node: Optional[Node], val: int) -> Union[Node, None]:
        if node is None:
            return None

        if node.val == val:
            return node
        elif node.val > val:
            return self.find_value(node.left, val)
        else:
            return self.find_value(node.right, val)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = Node(val=4)
        i1 = Node(val=1)
        i0 = Node(val=3, left=i1, right=i2)

        self.assertEqual(self.solution.find_value(node=i0, val=1), i1)

    def test_2(self):
        i4 = Node(val=10)
        i3 = Node(val=8)
        i2 = Node(val=9, left=i3, right=i4)
        i1 = Node(val=5)
        i0 = Node(val=7, left=i1, right=i2)

        self.assertEqual(self.solution.find_value(node=i0, val=9), i2)

    def test_3(self):
        i2 = Node(val=9)
        i1 = Node(val=6)
        i0 = Node(val=8, left=i1, right=i2)

        self.assertEqual(self.solution.find_value(node=i0, val=7), None)


if __name__ == "__main__":
    unittest.main()
