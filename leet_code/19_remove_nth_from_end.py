# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 39 ms, faster than 43.44% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.3 MB, less than 14.73 % of Python3 online submissions for Remove Nth Node From End of List.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        front_node: ListNode = head
        back_node: ListNode = head

        while n > 0:
            front_node = front_node.next
            n -= 1

        if not front_node:
            return head.next

        while front_node.next:
            back_node = back_node.next
            front_node = front_node.next

        if front_node:
            back_node.next = back_node.next.next
        else:
            head = head.next

        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.service = Solution()

    # def test_1(self):
    #     n4 = ListNode(5)
    #     n3 = ListNode(4, n4)
    #     n2 = ListNode(3, n3)
    #     n1 = ListNode(2, n2)
    #     n0 = ListNode(1, n1)

    #     self.assertEqual(self.service.removeNthFromEnd(n0, 2), n0)

    # def test_2(self):
    #     n0 = ListNode(1)

    #     self.assertEqual(self.service.removeNthFromEnd(n0, 1), None)

    # def test_3(self):
    #     n1 = ListNode(2)
    #     n0 = ListNode(1, n1)

    #     self.assertEqual(self.service.removeNthFromEnd(n0, 1), n0)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum(' '), 1)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('au'), 2)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('dvdf'), 3)

    # def test_1(self):
    #     self.assertEqual(self.service.twoSum('aabaab!bb'), 3)

if __name__ == "__main__":
    unittest.main()
