# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next
# pointer points to an earlier node, so as to make a loop in the linked list.

# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def cycle_node(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return None

        nodes: set[Optional[ListNode]] = set()

        while list.next:
            if list in nodes:
                return list

            nodes.add(list)
            list = list.next

        return None


class Solution2:
    def cycle_node(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if list is None or list.next is None:
            return None

        fast: Optional[ListNode] = list
        slow: Optional[ListNode] = list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None

        slow = list

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return fast


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_1(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i2.next = i0

        self.assertEqual(self.solution.cycle_node(i0), i0)

    def test_2(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution.cycle_node(i0), None)

    def test_3(self):
        i0 = ListNode(1)
        i0.next = i0

        self.assertEqual(self.solution.cycle_node(i0), i0)

    def test_4(self):
        i4 = ListNode(5)
        i3 = ListNode(4, i4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i4.next = i2

        self.assertEqual(self.solution.cycle_node(i0), i2)

    def test_5(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i2.next = i0

        self.assertEqual(self.solution2.cycle_node(i0), i0)

    def test_6(self):
        i2 = ListNode(3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)

        self.assertEqual(self.solution2.cycle_node(i0), None)

    def test_7(self):
        i0 = ListNode(1)
        i0.next = i0

        self.assertEqual(self.solution2.cycle_node(i0), i0)

    def test_8(self):
        i4 = ListNode(5)
        i3 = ListNode(4, i4)
        i2 = ListNode(3, i3)
        i1 = ListNode(2, i2)
        i0 = ListNode(1, i1)
        i4.next = i2

        self.assertEqual(self.solution2.cycle_node(i0), i2)

if __name__ == "__main__":
    unittest.main()
