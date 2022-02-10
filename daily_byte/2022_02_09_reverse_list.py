# This question is asked by Facebook.
# Given a linked list, containing unique values, reverse it, and return the result.
#
# Ex: Given the following linked lists...
# 1 -> 2 -> 3 -> null, return a reference to the node that contains 3 which points to a list that looks like the following: 3 -> 2 -> 1 -> null
# 7 -> 15 -> 9 -> 2 -> null, return a reference to the node that contains 2 which points to a list that looks like the following: 2 -> 9 -> 15 -> 7 -> null
# 1 -> null, return a reference to the node that contains 1 which points to a list that looks like the following: 1 -> null

from typing import Optional, List
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self

        while(temp):
            print(temp.val)
            temp = temp.next


class Solution:
    def reverse(self, list: Optional[ListNode]) -> Optional[ListNode]:
        previous_node: Optional[ListNode] = None
        current_node: Optional[ListNode] = list

        while current_node:
            next_node: Optional[ListNode] = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node


class Solution2:
    def reverse(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return list

        rest = self.reverse(list.next)

        list.next.next = list
        list.next = None

        return rest


class Solution3:
    def reverse(self, list: Optional[ListNode]) -> Optional[ListNode]:
        stack: List[ListNode] = []
        head: Optional[ListNode] = list

        while head:
            stack.append(head)
            head = head.next

        head = node = stack.pop()

        while len(stack) > 0:
            temp = stack.pop()
            node.next = temp
            node = temp

        node.next = None

        return head



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        i0 = ListNode(1)

        self.assertEqual(self.solution.reverse(i0), i0)

    def test_2(self):
        i3 = ListNode(2)
        i2 = ListNode(9, i3)
        i1 = ListNode(15, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution.reverse(i0), i3)
        self.assertEqual(i3.next, i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

    def test_3(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.reverse(i0), i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

    def test_4(self):
        i0 = ListNode(1)

        self.assertEqual(self.solution2.reverse(i0), i0)

    def test_5(self):
        i3 = ListNode(2)
        i2 = ListNode(9, i3)
        i1 = ListNode(15, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution2.reverse(i0), i3)
        self.assertEqual(i3.next, i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

    def test_6(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution2.reverse(i0), i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

    def test_7(self):
        i0 = ListNode(1)

        self.assertEqual(self.solution3.reverse(i0), i0)

    def test_8(self):
        i3 = ListNode(2)
        i2 = ListNode(9, i3)
        i1 = ListNode(15, i2)
        i0 = ListNode(7, i1)

        self.assertEqual(self.solution3.reverse(i0), i3)
        self.assertEqual(i3.next, i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

    def test_9(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution3.reverse(i0), i2)
        self.assertEqual(i2.next, i1)
        self.assertEqual(i1.next, i0)
        self.assertEqual(i0.next, None)

if __name__ == "__main__":
    unittest.main()
