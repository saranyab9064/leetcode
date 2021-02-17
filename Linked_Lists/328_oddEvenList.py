# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # declare two pointers 
        odd =  head
        even  = head.next
        odd_head = odd
        even_head = even
        # when the second pointer is not null segregate the odd node value to odd head and even node value to even head and incr the ptr
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            # point the odd node to even head
        odd.next = even_head
        return head
        
    
