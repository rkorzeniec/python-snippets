# This question is asked by Amazon.
# Given a non-empty linked list, return the middle node of the list.
# If the linked list contains an even number of elements, return the node closer to the end.
#
# 1 -> 2 -> 3 -> null, return 2
# 1 -> 2 -> 3 -> 4 -> null, return 3
# 1 -> null, return 1

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        list_length: int = 1
        head: Optional[ListNode] = list

        while head.next:
            head = head.next
            list_length += 1

        middle: int = list_length // 2 + 1

        head = list

        for _index in range(1, middle):
            head = head.next

        return head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.middle_node(i0), i1)

    def test_2(self):
        i3 = ListNode(4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.middle_node(i0), i2)

    def test_3(self):
        i0 = ListNode(1)

        self.assertEqual(self.solution.middle_node(i0), i0)

if __name__ == "__main__":
    unittest.main()
