# This question is asked by Microsoft.
# Given a linked list, containing unique numbers, return whether or not it has a cycle.
# Note: a cycle is a circular arrangement(i.e. one node points back to a previous node)
#
# 1 -> 2 -> 3 -> 1 -> true (3 points back to 1)
# 1 -> 2 -> 3 -> false
# 1 -> 1 true (1 points to itself)

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_circular(self, list: Optional[ListNode]) -> bool:
        if list is None or list.next is None:
            return False

        node_values: set[int] = set()

        while list.next:
            if list.val in node_values:
                return True

            node_values.add(list.val)
            list = list.next

        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i2.next = i0

        self.assertEqual(self.solution.is_circular(i0), True)

    def test_2(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.is_circular(i0), False)

    def test_3(self):
        i0 = ListNode(1)
        i0.next = i0

        self.assertEqual(self.solution.is_circular(i0), True)

if __name__ == "__main__":
    unittest.main()
