# frozen_string_literal: true

# Given two binary trees, return whether or not the two trees are identical.
# Note: identical meaning they exhibit the same structure and the same values at each node.

# Ex: Given the following trees...
#         2
#        / \
#       1   3
#     2
#    / \
#   1   3

# return true.

# Ex: Given the following trees...

#         1
#          \
#           9
#            \
#            18
#     1
#    /
#   9
#    \
#     18

# return false.

# Ex: Given the following trees...

#         2
#        / \
#       3   1
#     2
#    / \
#   1   3
# return false.

import unittest
from typing import Optional


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

    def is_equal(self, node1: Optional[Node], node2: Optional[Node]) -> None:
        if not node1 and node2:
            return False

        if node1 and not node2:
            return False

        if not node1 and not node2:
            return True

        if node1.val != node2.val:
            return False

        return self.is_equal(node1.left, node2.left) and self.is_equal(node1.right, node2.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        n3 = Node(val=3)
        n1 = Node(val=1)
        n2 = Node(val=2, left=n1, right=n3)

        k3 = Node(val=3)
        k1 = Node(val=1)
        k2 = Node(val=2, left=k1, right=k3)

        self.assertTrue(self.bst.is_equal(n2, k2))

    def test_2(self):
      n3 = Node(val=3)
      n1 = Node(val=1)
      n2 = Node(val=2, left=n3, right=n1)

      k3 = Node(val=3)
      k1 = Node(val=1)
      k2 = Node(val=2, left=k1, right=k3)

      self.assertFalse(self.bst.is_equal(n2, k2))


if __name__ == "__main__":
    unittest.main()
