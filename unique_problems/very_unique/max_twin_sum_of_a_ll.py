# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tort = head
        hare = head
        hashmap = {}
        i = 0
        ans = 0
        found_mid = 1
        while tort != None:
            if hare == None:
                if found_mid:
                    lp = i - 1
                    found_mid = 0
                ans = max(ans, hashmap[lp] + tort.val)
                lp -= 1
                # you have reached the end, time to look for twins of tort
                # tort is at n/2 pos
            # hare moves twice the speed
            else:
                hare = hare.next.next
                hashmap[i] = tort.val
            tort = tort.next
            i += 1
        return ans
