# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        
        while p != None and p.next != None:
            if p.val == p.next.val:
                q = p.next.next
                if q is None:
                    p.next = None
                    break
                p.next = q
            if p.val != p.next.val:
                p = p.next
        return head
