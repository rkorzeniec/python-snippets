# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional, List
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 62 ms, faster than 19.28% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 31.44 % of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        sorted_nodes: List[ListNode] = []
        current_list1_node: Optional[ListNode] = list1
        current_list2_node: Optional[ListNode] = list2

        while True:
            if current_list1_node is None and current_list2_node is None:
                break

            elif current_list1_node is None:
                sorted_nodes.append(current_list2_node)
                current_list2_node = current_list2_node.next

            elif current_list2_node is None:
                sorted_nodes.append(current_list1_node)
                current_list1_node = current_list1_node.next

            elif current_list1_node.val <= current_list2_node.val:
                sorted_nodes.append(current_list1_node)
                current_list1_node = current_list1_node.next

            else:
                sorted_nodes.append(current_list2_node)
                current_list2_node = current_list2_node.next

        for node_index in range(len(sorted_nodes) - 1):
            sorted_nodes[node_index].next = sorted_nodes[node_index + 1]

        [print(x.val) for x in sorted_nodes]

        return sorted_nodes[0]


# Runtime: 67 ms, faster than 13.16% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.5 MB, less than 31.44 % of Python3 online submissions for Merge Two Sorted Lists.
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        merged_list = self.merge_lists(list1, list2)

        return merged_list

    def merge_lists(self, list1_node: Optional[ListNode], list2_node: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        if list1_node is None:
            return list2_node

        if list2_node is None:
            return list1_node

        if list1_node.val <= list2_node.val:
            result = list1_node
            result.next = self.merge_lists(list1_node.next, list2_node)
        else:
            result = list2_node
            result.next = self.merge_lists(list1_node, list2_node.next)

        return result


# Runtime: 43 ms, faster than 44.60% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.5 MB, less than 31.44 % of Python3 online submissions for Merge Two Sorted Lists.
class Solution3:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node: Optional[ListNode] = ListNode()
        current_mode: Optional[ListNode] = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                current_mode.next = list1
                list1 = list1.next

            else:
                current_mode.next = list2
                list2 = list2.next

            current_mode = current_mode.next

        if list1:
            current_mode.next = list1
        elif list2:
            current_mode.next = list2

        return dummy_node.next



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_1(self):
        i2 = ListNode(4)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        j2 = ListNode(4)
        j1 = ListNode(3, j2)
        j0 = ListNode(1, j1)

        self.assertEqual(self.solution.mergeTwoLists(i0, j0), i0)
        self.assertEqual(self.solution2.mergeTwoLists(i0, j0), i0)
        self.assertEqual(self.solution3.mergeTwoLists(i0, j0), i0)

    def test_2(self):
        self.assertEqual(self.solution.mergeTwoLists(None, None), None)
        self.assertEqual(self.solution2.mergeTwoLists(None, None), None)
        self.assertEqual(self.solution3.mergeTwoLists(None, None), None)

    def test_3(self):
        k0 = ListNode(0)

        self.assertEqual(self.solution.mergeTwoLists(None, k0), k0)
        self.assertEqual(self.solution2.mergeTwoLists(None, k0), k0)
        self.assertEqual(self.solution3.mergeTwoLists(None, k0), k0)

    def test_5(self):
        i0 = ListNode(5)

        j2 = ListNode(4)
        j1 = ListNode(2, j2)
        j0 = ListNode(1, j1)

        self.assertEqual(self.solution.mergeTwoLists(i0, j0), j0)
        self.assertEqual(self.solution2.mergeTwoLists(i0, j0), j0)
        self.assertEqual(self.solution3.mergeTwoLists(i0, j0), j0)


if __name__ == "__main__":
    unittest.main()
