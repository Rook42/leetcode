from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def ListNode(self, data):
        try:
            return ListNode(data[0], ListNode.ListNode(self, data[1:]))
        except IndexError:
            return ListNode(data[0], None)


class Solution:

    def getDecimalValue(self, head: ListNode) -> int:
        out = 0
        out << 1
        if head.val == 1:
            out += 1
        return self.helper(head.next, out)

    def helper(self, head: ListNode, working):
        if head == None:
            return working
        working = working << 1
        if head.val == 1:
            working += 1
        return self.helper(head.next, working)
