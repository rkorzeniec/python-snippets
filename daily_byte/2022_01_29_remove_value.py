# This question is asked by Google.
# Given a linked list and a value, remove all nodes containing the provided value,
# and return the resulting list.
#
# 1 -> 2 -> 3 -> null, value = 3, return 1 -> 2 -> null
# 8 -> 1 -> 1 -> 4 -> 12 -> null, value = 1, return 8 -> 4 -> 12 -> null
# 7 -> 12 -> 2 -> 9 -> null, value = 7, return 12 -> 2 -> 9 -> null

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_value(self, list: Optional[ListNode], n: int) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        if list.val == n:
            return list.next

        head: Optional[ListNode] = list
        tail: Optional[ListNode] = ListNode(next=head)

        while head:
            if head.val == n:
                while head and head.val == n:
                    head = head.next

            tail.next = head
            tail = tail.next

            if head is not None:
                head = head.next

        return list

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.remove_value(i0, 3), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, None)

    def test_2(self):
        i4 = ListNode(12)
        i3 = ListNode(4, i4)
        i2 = ListNode(1, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(8, i1)

        self.assertEqual(self.solution.remove_value(i0, 1), i0)
        self.assertEqual(i0.next, i3)
        self.assertEqual(i3.next, i4)
        self.assertEqual(i4.next, None)

    def test_3(self):
        i3 = ListNode(9)
        i2 = ListNode(2, i3)
        i1 = ListNode(12, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution.remove_value(i0, 7), i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, i3)
        self.assertEqual(i3.next, None)

if __name__ == "__main__":
    unittest.main()
