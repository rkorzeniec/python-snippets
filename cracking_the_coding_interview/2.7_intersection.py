# Given two (singly) linked lists, determine if the two lists intersect.
# Return the inter­ secting node.
#
# Note that the intersection is defined based on reference, not value.
#
# That is, if the kth node of the first linked list is the exact same node
# (by reference) as the jth node of the second linked list,
# then they are intersecting.

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListResult:
    def __init__(self, tail=None, length=0):
        self.tail = tail
        self.length = length


class Solution:
    def intersection(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return None

        list1_result = self.list_result(list1)
        list2_result = self.list_result(list2)

        if list1_result.tail != list2_result.tail:
            return None

        if list1_result.length > list2_result.length:
            for i in range(list1_result.length - list2_result.length):
                list1 = list1.next
        else:
            for i in range(list2_result.length - list1_result.length):
                list2 = list2.next

        while list1 and list2:
            if list1 == list2:
                return list1

            list1 = list1.next
            list2 = list2.next

        return None

    def list_result(self, list: Optional[ListNode]) -> Optional[ListResult]:
        count: int = 0

        while list:
            count += 1
            list = list.next

        return ListResult(list, count)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i5 = ListNode(0)
        i4 = ListNode(1, i5)
        i3 = ListNode(2, i4)
        i2 = ListNode(2, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(0, i1)

        self.assertEqual(self.solution.intersection(i0, i3), i3)

    def test_2(self):
        i6 = ListNode(0)
        i5 = ListNode(1, i6)

        i4 = ListNode(2, i5)
        i3 = ListNode(3, i4)
        i2 = ListNode(2, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(0, i1)

        self.assertEqual(self.solution.intersection(i0, i5), i5)

    def test_3(self):
        i3 = ListNode(3)
        i2 = ListNode(2, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(0, i1)

        j3 = ListNode(3)
        j2 = ListNode(2, j3)
        j1 = ListNode(1, j2)
        j0 = ListNode(0, j1)

        self.assertEqual(self.solution.intersection(i0, j0), None)

if __name__ == "__main__":
    unittest.main()
