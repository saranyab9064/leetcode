
"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:
            return head
        # declare the current ptr
        curr = head
        # determine the length of the linked list
        n = 1
        while curr.next:
            n = n + 1
            curr = curr.next
        print(n)
        
        # we have point last node to first
        curr.next = head
        # go till that node and remove the link and point to null
        # to optimise the k value and no of rotation
        k = k%n
        k = n - k
        while k:
            curr = curr.next
            k = k-1
        # remove the link
        head = curr.next
        curr.next = None
        
        return head
        
        
