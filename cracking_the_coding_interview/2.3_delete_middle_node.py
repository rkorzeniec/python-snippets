# Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.
#
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e - >f

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_mid_node(node: Optional[ListNode]) -> bool:
        if node is None or node.next is None:
            return False

        node.val = node.next.val
        node.next = node.next.next

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i5 = ListNode(6)
        i4 = ListNode(5, i5)
        i3 = ListNode(4, i4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.delete_mid_node(i2), True)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i3)
        self.assertEqual(i3.next, i4)
        self.assertEqual(i4.next, i5)
        self.assertEqual(i5.next, None)

    def test_2(self):
        self.assertEqual(self.solution.delete_mid_node(None), False)

    def test_3(self):
        i1 = ListNode(2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.delete_mid_node(i1), False)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, None)


if __name__ == "__main__":
    unittest.main()
