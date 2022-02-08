# Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.
#
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e - >f

from tkinter import Y
from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_middle_node(self, list: Optional[ListNode], node: Optional[ListNode]) -> None:
        if list is None or node == list:
            return None

        head: Optional[ListNode] = list.next
        tail: Optional[ListNode] = list

        while head:
            if head == node:
                tail.next = head.next
            head = head.next
            tail = tail.next

        return tail


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

        self.assertEqual(self.solution.delete_middle_node(i0, i2), None)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i3)
        self.assertEqual(i3.next, i4)
        self.assertEqual(i4.next, i5)
        self.assertEqual(i5.next, None)

    def test_2(self):
        i1 = ListNode(2, None)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.delete_middle_node(i0, i0), None)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, None)


if __name__ == "__main__":
    unittest.main()
