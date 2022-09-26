# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None
        # first detect cycle
        t, h = head, head
        while h.next != None and h.next.next != None:
            t = t.next
            h = h.next.next

            if h == t:
                # cycle found
                t = head
                while h != t:
                    t = t.next
                    h = h.next
                return h
        return None
