# This question is asked by Apple.
# Given a potentially cyclical linked list where each value is unique,
# return the node at which the cycle starts.
# If the list does not contain a cycle, return null.
#
# 1 -> 2 -> 3, return null
# 1 -> 2 -> 3 -> 4 -> 5 -> 2 (5 points back to 2), return a reference to the node containing 2
# 1 -> 9 -> 3 -> 7 -> 7 (7 points to itself), return a reference to the node containing 7

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def staart_of_cycle(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return None

        node_values: set[int] = set()

        while list.next:
            if list.val in node_values:
                return list

            node_values.add(list.val)
            list = list.next

        return None

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.staart_of_cycle(i0), None)

    def test_2(self):
        i4 = ListNode(5)
        i3 = ListNode(4, i4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i4.next = i1

        self.assertEqual(self.solution.staart_of_cycle(i0), i1)

    def test_3(self):
        i3 = ListNode(7)
        i2 = ListNode(3, i3)
        i1 = ListNode(9, i2)
        i0 = ListNode(1, i1)
        i3.next = i3

        self.assertEqual(self.solution.staart_of_cycle(i0), i3)

if __name__ == "__main__":
    unittest.main()
