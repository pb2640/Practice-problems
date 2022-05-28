# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        curr = temp
        it = temp
        while curr != None:
            while it.next != None and it.next.val == val:
                it = it.next
            curr.next = it.next
            curr = it.next
            it = curr
        return temp.next
