# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        fast, slow = head, head
        stck = []
        while fast and fast.next:
            stck.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow and len(stck):
            if stck.pop() != slow.val:
                return False
            slow = slow.next
        return True
