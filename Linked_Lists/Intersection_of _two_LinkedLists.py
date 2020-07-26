# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA == None or headB == None):
            return None
        tempA = headA
        tempB = headB
        lenA = 0
        lenB = 0
        
        while tempA.next != None:
            lenA = lenA +1
            tempA = tempA.next
            
        while tempB.next != None:
            lenB = lenB +1
            tempB = tempB.next   
        
        diff = 0
        if lenA > lenB:
            tempA = headA
            tempB = headB
            diff = lenA - lenB
        else:
            tempA = headB
            tempB = headA
            diff = lenB - lenA  
        while diff > 0:
            tempA = tempA.next
            diff = diff - 1
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
        return tempA
        
        
        
        
        
