# frozen_string_literal: true

# Given a binary search tree, return the minimum difference between any two nodes in the tree.

# Ex: Given the following tree...
#         2
#        / \
#       3   1
# return 1.

# Ex: Given the following tree...
#         29
#        /  \
#      17   50
#     /     / \
#    1    42  59
# return 8.

# Ex: Given the following tree...
#         2
#          \
#          100
# return 98.

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

    def minimum_difference(self) -> int:
      return self._minimum_difference(self.root)

    def _minimum_difference(self, node: Optional[Node]) -> Optional[int]:
        if node is None:
            return None

        diffs = []

        if node.left:
            diffs.append(node.val - node.left.val)

        if node.right:
            diffs.append(node.right.val - node.val)

        diffs.append(self._minimum_difference(node.left))
        diffs.append(self._minimum_difference(node.right))
        diffs = [d for d in diffs if d]

        return min(diffs) if diffs else None



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(1)

        self.assertEqual(self.bst.minimum_difference(), 1)

    def test_2(self):
        self.bst.insert(29)
        self.bst.insert(17)
        self.bst.insert(1)
        self.bst.insert(50)
        self.bst.insert(42)
        self.bst.insert(59)

        self.assertEqual(self.bst.minimum_difference(), 8)

    def test_3(self):
        self.bst.insert(2)
        self.bst.insert(100)

        self.assertEqual(self.bst.minimum_difference(), 98)


if __name__ == "__main__":
    unittest.main()
