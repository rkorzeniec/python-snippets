# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node: ListNode = head
        sub_head_node: ListNode = head
        index = 0

        if head.next == None and n > 0:
            return None

        while current_node.next:
            current_node = current_node.next

            if index >= n:
                sub_head_node = sub_head_node.next

            index += 1

        sub_head_node.next = current_node

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
