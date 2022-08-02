# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt1 = ListNode("s")
        pt1.next = head
        pt2 = pt1
        while n > 0:
            pt2 = pt2.next
            n -= 1
        # the difference has been achieved
        # so, the pt1.next node has to be removed
        while pt2.next != None:
            pt2 = pt2.next
            pt1 = pt1.next
        temp = pt1.next.next
        pt1.next = temp
        if pt1.val == "s":
            return pt1.next
        else:
            return head
