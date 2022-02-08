# Implement an algorithm to find the kth to last element of a singly linked list.

from tkinter import Y
from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def kth_to_last(self, list: Optional[ListNode], k: int) -> Optional[ListNode]:
        if list is None:
            return list

        head: Optional[ListNode] = list
        tail: Optional[ListNode] = head

        for i in range(k):
            head = head.next

        while head.next:
            head = head.next
            tail = tail.next

        return tail


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.kth_to_last(i0, 0), i2)

    def test_2(self):
        i4 = ListNode(12)
        i3 = ListNode(1, i4)
        i2 = ListNode(4, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(8, i1)

        self.assertEqual(self.solution.kth_to_last(i0, 2), i2)

    def test_3(self):
        i3 = ListNode(7)
        i2 = ListNode(2, i3)
        i1 = ListNode(12, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution.kth_to_last(i0, 3), i0)

if __name__ == "__main__":
    unittest.main()
