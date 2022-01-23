# https://leetcode.com/problems/rotate-list

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 28 ms, faster than 98.68% of Python3 online submissions for Rotate List.
# Memory Usage: 14.3 MB, less than 60.07 % of Python3 online submissions for Rotate List.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or (head.next == None and k > 0):
            return head

        current_node: ListNode = head
        new_head: ListNode = head
        count: int = 1

        while current_node.next:
            current_node = current_node.next
            count += 1

        current_node.next = head

        if k > count:
            k %= count

        for i in range(count - k):
            current_node = current_node.next

        new_head = current_node.next
        current_node.next = None

        return new_head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        n4 = ListNode(5)
        n3 = ListNode(4, n4)
        n2 = ListNode(3, n3)
        n1 = ListNode(2, n2)
        n0 = ListNode(1, n1)

        self.assertEqual(self.solution.rotateRight(n0, 2), n3)

    def test_2(self):
        n2 = ListNode(2)
        n1 = ListNode(1, n2)
        n0 = ListNode(0, n1)

        self.assertEqual(self.solution.rotateRight(n0, 4), n2)


if __name__ == "__main__":
    unittest.main()
