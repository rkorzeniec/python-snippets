# Given a binary search tree, rearrange the tree such that it forms a linked list
# where all its values are in ascending order.

# Ex: Given the following tree...
#         5
#        / \
#       1   6

# return...
# 1
#  \
#   5
#    \
#     6

# Ex: Given the following tree...
#        5
#       / \
#     2    9
#    / \
#   1   3

# return...
# 1
#  \
#   2
#    \
#     3
#      \
#       5
#        \
#         9

# Ex: Given the following tree...
# 5
#  \
#   6

# return...
# 5
#  \
#   6


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
            self._pretty_print(node.right, prefix + ('│   ' if is_left else '    '), False)

        print(prefix + ('└── ' if is_left else '┌── ') + str(node.val))

        if node.left:
            self._pretty_print(node.left, prefix + ('    ' if is_left else '│   '), True)

    def convert(self) -> None:
        dummy_node = Node(None)
        self._previous_node = dummy_node

        self._inorder_traversal(self.root)

        self._previous_node.right = None
        self._previous_node.left = None

        return dummy_node.right

    def _inorder_traversal(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        self._inorder_traversal(node.left)

        self._previous_node.left = None
        self._previous_node.right = node
        self._previous_node = node

        self._inorder_traversal(node.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_1(self):
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(6)

        result = self.bst.convert()
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 6)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_2(self):
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.insert(9)
        self.bst.insert(1)
        self.bst.insert(3)

        result = self.bst.convert()
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 2)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 3)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 9)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_3(self):
        self.bst.insert(5)
        self.bst.insert(6)

        result = self.bst.convert()
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.left)

        result = result.right
        self.assertEqual(result.val, 6)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)


if __name__ == "__main__":
    unittest.main()
