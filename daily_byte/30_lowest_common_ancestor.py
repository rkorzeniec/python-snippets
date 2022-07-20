# frozen_string_literal: true

# Given a binary search tree that contains unique values and two nodes within the tree,
# a, and b, return their lowest common ancestor.

# NOTE: the lowest common ancestor of two nodes is the deepest node within the tree
# such that both nodes are descendants of it.

# Ex: Given the following tree...
#        7
#       / \
#     2    9
#    / \
#   1   5
# and a = 1, b = 9, return a reference to the node containing 7.

# Ex: Given the following tree...
#         8
#        / \
#       3   9
#      / \
#     2   6
# and a = 2, b = 6, return a reference to the node containing 3.

# Ex: Given the following tree...
#         8
#        / \
#       6   9
# and a = 6, b = 8, return a reference to the node containing 8.

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

    def ancestor(self, a: int, b: int) -> Optional[Node]:
        return self._ancestor(self.root, a, b)

    def _ancestor(self, node: Optional[Node], a: int, b: int) -> Optional[Node]:
        if node is None:
            return None

        if node.val == a or node.val == b:
            return node

        if a < node.val < b:
          return node

        if a < node.val and b < node.val:
          return self._ancestor(node.left, a, b)
        else:
          self._ancestor(node.right, a, b)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(9)
        self.bst.insert(1)
        self.bst.insert(5)

        self.assertEqual(self.bst.ancestor(1, 9).val, 7)

    def test_2(self):
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(9)
        self.bst.insert(2)
        self.bst.insert(6)

        self.assertEqual(self.bst.ancestor(2, 6).val, 3)

    def test_3(self):
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.ancestor(6, 8).val, 8)


if __name__ == "__main__":
    unittest.main()
