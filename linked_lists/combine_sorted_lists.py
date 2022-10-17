# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # base case
        head = ListNode(-1)
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1

        node1 = list1
        node2 = list2
        node = head
        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                node.next = node1
                node = node.next
                node1 = node1.next
            else:
                node.next = node2
                node = node.next
                node2 = node2.next
        while node2:
            node.next = node2
            node = node.next
            node2 = node2.next
        while node1:
            node.next = node1
            node = node.next
            node1 = node1.next
        return head.next
