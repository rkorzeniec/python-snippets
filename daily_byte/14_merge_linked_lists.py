# This question is asked by Apple.
# Given two sorted linked lists, merge them together in ascending order
# and return a reference to the merged list

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node: Optional[ListNode] = ListNode()
        current_node = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1:
            current_node.next = list1
        elif list2:
            current_node.next = list2

        # current_node = dummy_node.next
        # while current_node:
        #     print(current_node.val)
        #     current_node = current_node.next

        return dummy_node.next



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        j2 = ListNode(6)
        j1 = ListNode(5, j2)
        j0 = ListNode(4, j1)

        self.assertEqual(self.solution.merge_lists(i0, j0), i0)

    def test_2(self):
        i2 = ListNode(5)
        i1 = ListNode(3, i2)
        i0 = ListNode(1, i1)

        j2 = ListNode(6)
        j1 = ListNode(4, j2)
        j0 = ListNode(2, j1)

        self.assertEqual(self.solution.merge_lists(i0, j0), i0)

    def test_3(self):
        i2 = ListNode(7)
        i1 = ListNode(4, i2)
        i0 = ListNode(4, i1)

        j2 = ListNode(6)
        j1 = ListNode(5, j2)
        j0 = ListNode(1, j1)

        self.assertEqual(self.solution.merge_lists(i0, j0), j0)

if __name__ == "__main__":
    unittest.main()
