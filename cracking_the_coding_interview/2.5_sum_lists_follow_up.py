# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
#
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
#
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PartialSum:
    def __init__(self, sum: Optional[ListNode] = None, carry: int = 0):
        self.sum: Optional[ListNode] = sum
        self.carry: int = carry


class Solution:
    def sum(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        node1_length: int = self.list_length(node1)
        node2_length: int = self.list_length(node2)

        if node1_length < node2_length:
            node1 = self.pad_list(node1, node2_length - node1_length)
        else:
            node2 = self.pad_list(node2, node1_length - node2_length)

        sum: Optional[PartialSum] = self.add_lists(node1, node2)

        if sum.carry == 0:
            return sum.sum
        else:
            result: Optional[ListNode] = self.prepend(sum.sum, sum.carry)
            return result

    def add_lists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[PartialSum]:
        if node1 is None and node2 is None:
            return PartialSum()

        partial_result: Optional[PartialSum] = self.add_lists(node1.next, node2.next)
        sum: int = partial_result.carry + node1.val + node2.val

        result: Optional[ListNode] = self.prepend(partial_result, sum % 10)

        partial_result.sum = result
        partial_result.carry = sum // 10

        return partial_result

    def pad_list(self, node: Optional[ListNode], n: int=0):
        count: int = 0
        head: Optional[ListNode] = node

        while count < n:
            head = self.prepend(head, 0)

            count += 1

        return head


    def list_length(self, head: Optional[ListNode]) -> int:
        count: int = 0

        while head:
            count += 1
            head = head.next

        return count

    def prepend(self, node: Optional[PartialSum], value: int) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode(value)

        if node:
            head.next = node

        return head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        j2 = ListNode(5)
        j1 = ListNode(9, j2)
        j0 = ListNode(2, j1)

        i2 = ListNode(7)
        i1 = ListNode(1, i2)
        i0 = ListNode(6, i1)

        result = self.solution.sum(i0, j0)
        self.assertEqual(result.val, 9)
        result = result.next
        self.assertEqual(result.val, 1)
        result = result.next
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next, None)

    def test_2(self):
        j2 = ListNode(7)
        j1 = ListNode(6, j2)
        j0 = ListNode(5, j1)

        i3 = ListNode(4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        result = self.solution.sum(i0, j0)
        self.assertEqual(result.val, 1)
        result = result.next
        self.assertEqual(result.val, 8)
        result = result.next
        self.assertEqual(result.val, 0)
        result = result.next
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next, None)

if __name__ == "__main__":
    unittest.main()
