# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
#
# If x is contained within the list,
# the values of x only need to be after the elements less than x (see below).
#
# The partition element x can appear anywhere in the "right partition"
# it does not need to appear between the left and right partitions.
#
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 5 -> 5 -> 8 -> 10

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, node: Optional[ListNode], pivot: int) -> Optional[ListNode]:
        if node is None or node.next is None:
            return node

        head: Optional[ListNode] = node
        tail: Optional[ListNode] = node

        while node:
            next: Optional[ListNode] = node.next

            if node.val < pivot:
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node

            node = next

        tail.next = None

        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i6 = ListNode(1)
        i5 = ListNode(2, i6)
        i4 = ListNode(10, i5)
        i3 = ListNode(5, i4)
        i2 = ListNode(8, i3)
        i1 = ListNode(5, i2)
        i0 = ListNode(3, i1)

        self.assertEqual(self.solution.partition(i0, 5), i6)
        self.assertEqual(i6.next, i5)
        self.assertEqual(i5.next, i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, i3)
        self.assertEqual(i3.next, i4)
        self.assertEqual(i4.next, None)

if __name__ == "__main__":
    unittest.main()
