# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases such as removing the first node
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

        