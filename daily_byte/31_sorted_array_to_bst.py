# frozen_string_literal: true

# Given an array of numbers sorted in ascending order,
# return a height-balanced binary search tree using every number from the array.

# NOTE: height-balanced meaning that the level of any node’s two subtrees
# should not differ by more than one.

# Ex: Given the following nums...
# nums = [1, 2, 3] return a reference to the following tree...
#        2
#       /  \
#      1    3

# Ex: Given the following nums...
# nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
#         3
#        / \
#       2   5
#      /   / \
#     1   4   6

from typing import Optional
import unittest


class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val: int, node: Optional[Node]) -> None:
        if node is None:
            return Node(val)

        if node.val == val:
            return node

        if node.val < val:
            node.right = self._insert(val, node.right)
        else:
            node.left = self._insert(val, node.left)

        return node

    def pretty_print(self):
        self._pretty_print(self.root)

    def _pretty_print(self, node=None, prefix='', is_left=True):
        if node.right:
            self._pretty_print(node.right, prefix +
                               ('│   ' if is_left else '    '), False)

        print(prefix + ('└── ' if is_left else '┌── ') + str(node.val))

        if node.left:
            self._pretty_print(node.left, prefix +
                               ('    ' if is_left else '│   '), True)

    def populate(self, nums: list) -> None:
        if not nums:
          return None

        pivot = len(nums) // 2

        self.insert(nums[pivot])
        self.populate(nums[:pivot])
        self.populate(nums[pivot + 1:])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        nums = [1, 2, 3]

        self.bst.populate(nums)
        self.bst.pretty_print()

    def test_2(self):
        nums = [1, 2, 3, 4, 5, 6]

        self.bst.populate(nums)
        self.bst.pretty_print()


if __name__ == "__main__":
    unittest.main()
