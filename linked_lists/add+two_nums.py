# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def reverse(head):
        #     prev = None
        #     curr = head
        #     while(curr!=None):
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp
        #     return prev
        def calc(head):
            i = 0
            num = 0
            while(head):
                num+=head.val*(10**i)
                i+=1
                head = head.next
            return num
                
        l1 = calc(l1)
        l2 = calc(l2)
        num = l1+l2
        if(num==0):
            return ListNode(0)
        ref = ListNode(-1)
        node = ref
        while(num!=0):
            add = ListNode(num%10)
            num = num//10
            node.next = add
            node = add
        return ref.next
            
            
        