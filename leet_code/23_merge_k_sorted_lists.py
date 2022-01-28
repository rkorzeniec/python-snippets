# https://leetcode.com/problems/merge-k-sorted-lists

from typing import Optional, List
from heapq import heapify, heappush, heappop
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 116 ms, faster than 68.07% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 82.20 % of Python3 online submissions for Merge k Sorted Lists.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None

        lists_length = len(lists)

        if lists_length < 1:
            return None
        elif lists_length == 1:
            return lists[0]

        mid = lists_length // 2

        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge_lists(left, right)

    def merge_lists(self, list1_node: Optional[ListNode], list2_node: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node: Optional[ListNode] = ListNode()
        current_mode: Optional[ListNode] = dummy_node

        while list1_node and list2_node:
            if list1_node.val < list2_node.val:
                current_mode.next = list1_node
                list1_node = list1_node.next

            else:
                current_mode.next = list2_node
                list2_node = list2_node.next

            current_mode = current_mode.next

        if list1_node:
            current_mode.next = list1_node
        elif list2_node:
            current_mode.next = list2_node

        # current_node = dummy_node.next
        # while current_node:
        #     print(current_node.val)
        #     current_node = current_node.next
        # print()

        return dummy_node.next


# Runtime: 225 ms, faster than 18.96% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.6 MB, less than 93.20 % of Python3 online submissions for Merge k Sorted Lists.
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [(node.val, index) for index, node in enumerate(lists) if node]
        heapify(min_heap)

        head_node: Optional[ListNode] = ListNode()
        tail_node: Optional[ListNode] = head_node

        while min_heap:
            _, node_idx = heappop(min_heap)

            tail_node.next = lists[node_idx]
            tail_node = tail_node.next
            lists[node_idx] = lists[node_idx].next

            if lists[node_idx]:
                heappush(min_heap, (lists[node_idx].val, node_idx))

        return head_node.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        i2 = ListNode(5)
        i1 = ListNode(4, i2)
        i0 = ListNode(1, i1)

        j2 = ListNode(4)
        j1 = ListNode(3, j2)
        j0 = ListNode(1, j1)

        k1 = ListNode(6)
        k0 = ListNode(2, k1)

        # self.assertEqual(self.solution.mergeKLists([i0, j0, k0]), j0)
        self.assertEqual(self.solution2.mergeKLists([i0, j0, k0]), j0)

    def test_2(self):
        # self.assertEqual(self.solution.mergeKLists([]), None)
        self.assertEqual(self.solution2.mergeKLists([]), None)

    def test_3(self):
        # self.assertEqual(self.solution.mergeKLists([None]), None)
        self.assertEqual(self.solution2.mergeKLists([None]), None)


if __name__ == "__main__":
    unittest.main()
