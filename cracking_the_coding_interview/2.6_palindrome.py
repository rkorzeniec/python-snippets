# Implement a function to check if a linked list is a palindrome.

from typing import List, Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def palindrome(self, head: Optional[ListNode]) -> bool:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head

        stack: List[Optional[ListNode]] = []

        while fast and fast.next:
            stack.append(slow)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            node: Optional[ListNode] = stack.pop()

            if node.val != slow.val:
                return False

            slow = slow.next

        return True


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

        self.assertEqual(self.solution.palindrome(i0), True)

    def test_2(self):
        i6 = ListNode(0)
        i5 = ListNode(1, i6)
        i4 = ListNode(2, i5)
        i3 = ListNode(3, i4)
        i2 = ListNode(2, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(0, i1)

        self.assertEqual(self.solution.palindrome(i0), True)

    def test_3(self):
        i3 = ListNode(3)
        i2 = ListNode(2, i3)
        i1 = ListNode(1, i2)
        i0 = ListNode(0, i1)

        self.assertEqual(self.solution.palindrome(i0), False)

if __name__ == "__main__":
    unittest.main()
