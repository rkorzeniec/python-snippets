# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
#
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sum(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        result_head: Optional[ListNode] = ListNode()
        result: Optional[ListNode] = result_head
        carry: int = 0

        while node1 and node2:
            sum_node: Optional[ListNode] = ListNode()
            result.next = sum_node

            sum: int = carry

            if node1:
                sum += node1.val
                node1 = node1.next

            if node2:
                sum += node2.val
                node2 = node2.next

            carry = sum // 10

            sum_node.val = sum % 10
            result = sum_node


        return result_head.next


class Solution2:
    def sum(self, node1: Optional[ListNode], node2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if node1 is None and node2 is None and carry == 0:
            return None

        result: Optional[ListNode] = ListNode()
        sum: int = carry

        if node1:
            sum += node1.val
            node1 = node1.next

        if node2:
            sum += node2.val
            node2 = node2.next

        result.val = sum % 10

        if node1 or node2:
            carry = sum // 10

            next_result: Optional[ListNode] = self.sum(node1, node2, carry)
            result.next = next_result

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        j2 = ListNode(2)
        j1 = ListNode(9, j2)
        j0 = ListNode(5, j1)

        i2 = ListNode(6)
        i1 = ListNode(1, i2)
        i0 = ListNode(7, i1)

        result = self.solution.sum(i0, j0)
        self.assertEqual(result.val, 2)
        result = result.next
        self.assertEqual(result.val, 1)
        result = result.next
        self.assertEqual(result.val, 9)
        self.assertEqual(result.next, None)

    def test_2(self):
        j2 = ListNode(2)
        j1 = ListNode(9, j2)
        j0 = ListNode(5, j1)

        i2 = ListNode(6)
        i1 = ListNode(1, i2)
        i0 = ListNode(7, i1)

        result = self.solution2.sum(i0, j0)
        self.assertEqual(result.val, 2)
        result = result.next
        self.assertEqual(result.val, 1)
        result = result.next
        self.assertEqual(result.val, 9)
        self.assertEqual(result.next, None)

    def test_3(self):
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

    def test_4(self):
        j2 = ListNode(5)
        j1 = ListNode(9, j2)
        j0 = ListNode(2, j1)

        i2 = ListNode(7)
        i1 = ListNode(1, i2)
        i0 = ListNode(6, i1)

        result = self.solution2.sum(i0, j0)
        self.assertEqual(result.val, 9)
        result = result.next
        self.assertEqual(result.val, 1)
        result = result.next
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next, None)

if __name__ == "__main__":
    unittest.main()
