"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        node = head
        hashmap = {}

        while node != None:
            if node not in hashmap:
                hashmap[node] = Node(node.val)
            if node.next:
                if node.next not in hashmap:
                    hashmap[node.next] = Node(node.next.val)
                hashmap[node].next = hashmap[node.next]
            else:
                hashmap[node].next = None
            if node.random:
                if node.random not in hashmap:
                    hashmap[node.random] = Node(node.random.val)
                hashmap[node].random = hashmap[node.random]
            else:
                hashmap[node].random = None

            node = node.next
        return hashmap[head]
