# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        node = head
        record = set()
        while node:
            if node in record:
                return True
            record.add(node)
            node = node.next

        return False
