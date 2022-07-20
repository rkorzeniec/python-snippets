# frozen_string_literal: true

# Given a binary search tree,
# return its mode (you may assume the answer is unique).
# If the tree is empty, return -1.

# NOTE: the mode is the most frequently occurring value in the tree.

# Ex: Given the following tree...
#         2
#        / \
#       1   2
# return 2.

# Ex: Given the following tree...
#          7
#         / \
#       4     9
#      / \   / \
#     1   4 8   9
#                \
#                 9
# return 9.

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

        if node.val <= val:
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

    def mode(self) -> int:
        self.cache = {}

        self.inorder(self.root)

        return max(self.cache.items(), key=lambda x: x[1])[0]

    def inorder(self, node: Optional[Node]) -> None:
        if node is None:
            return

        self.inorder(node.left)
        self.cache[node.val] = self.cache.get(node.val, 0) + 1
        self.inorder(node.right)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        self.bst.insert(2)
        self.bst.insert(1)
        self.bst.insert(2)

        self.assertEqual(self.bst.mode(), 2)

    def test_2(self):
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(9)
        self.bst.insert(8)
        self.bst.insert(9)
        self.bst.insert(9)

        self.assertEqual(self.bst.mode(), 9)


if __name__ == "__main__":
    unittest.main()
