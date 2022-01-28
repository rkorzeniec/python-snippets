# This question is asked by Facebook.
# Given a linked list and a value n,
# remove the nth to last node and return the resulting list.
#
# 1 -> 2 -> 3 -> null, n = 1, return 1 -> 2 -> null
# 1 -> 2 -> 3 -> null, n = 2, return 1 -> 3 -> null
# 1 -> 2 -> 3 -> null, n = 3, return 2 -> 3 -> null

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth(self, list: Optional[ListNode], n: int) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        list_length: int = 1
        head: Optional[ListNode] = list

        while head.next:
            head = head.next
            list_length += 1

        if n == list_length:
            return list.next

        head = list

        for _index in range(1, list_length - n):
            head = head.next

        head.next = head.next.next

        return list

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.remove_nth(i0, 1), i0)

    def test_2(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.remove_nth(i0, 2), i0)

    def test_3(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.remove_nth(i0, 3), i1)

if __name__ == "__main__":
    unittest.main()
