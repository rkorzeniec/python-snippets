# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def dedup(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        node_values: set[int] = set()
        head: Optional[ListNode] = list
        previous: Optional[ListNode] = ListNode(next = head)

        while head:
            if head.val in node_values:
                previous.next = head.next
            else:
                node_values.add(head.val)
                previous = head

            head = head.next

        return list

# How would you solve this problem if a temporary buffer is not allowed?
class Solution2:
    def dedup(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        head: Optional[ListNode] = list
        runner: Optional[ListNode] = None
        previous: Optional[ListNode] = None

        while head:
            runner = head.next
            previous = head

            while runner:
                if head.val == runner.val:
                    previous.next = runner.next

                runner = runner.next
                previous = previous.next

            head = head.next

        return list


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, None)

    def test_2(self):
        i4 = ListNode(12)
        i3 = ListNode(1, i4)
        i2 = ListNode(4, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(8, i1)

        self.assertEqual(self.solution.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, i4)
        self.assertEqual(i4.next, None)

    def test_3(self):
        i3 = ListNode(7)
        i2 = ListNode(2, i3)
        i1 = ListNode(12, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, None)

    def test_4(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution2.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, None)

    def test_5(self):
        i4 = ListNode(12)
        i3 = ListNode(1, i4)
        i2 = ListNode(4, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(8, i1)

        self.assertEqual(self.solution2.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, i4)
        self.assertEqual(i4.next, None)

    def test_6(self):
        i3 = ListNode(7)
        i2 = ListNode(2, i3)
        i1 = ListNode(12, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution2.dedup(i0), i0)
        self.assertEqual(i0.next, i1)
        self.assertEqual(i1.next, i2)
        self.assertEqual(i2.next, None)

if __name__ == "__main__":
    unittest.main()
