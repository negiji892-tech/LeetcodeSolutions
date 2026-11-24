# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        size = 0
        curr = head
        while curr is not None:
            curr = curr.next
            size+=1

        indexToSearch = size - n
        if indexToSearch == 0:
            return head.next
        prev = head
        i=1
        while i<indexToSearch:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head

        