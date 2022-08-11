#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        if(ImmutableListNode.getNext(head)):
            self.printLinkedListInReverse(ImmutableListNode.getNext(head))
            
        ImmutableListNode.printValue(head)
        """
        :type head: ImmutableListNode
        :rtype: None
        """
		