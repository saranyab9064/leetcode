#============================================================================
# Name        : 01_Merge_Two_Sorted_Lists.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):

"""
# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 202 cases passed out of 208 cases
        # create a dummynode (sortednode)
        temp = sortednode = ListNode(0)
        # check whether l1 and l2 is empty
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 and l2:
            if l1.val <= l2.val:
                sortednode = l1
                l1 = sortednode.next
            else:
                sortednode = l2
                l2 = sortednode.next
        new_head = sortednode
        while (l1 and l2):
            if l1.val <= l2.val:
                sortednode.next = l1
                sortednode = l1
                l1 = sortednode.next
            else:
                sortednode.next = l2
                sortednode = l2
                l2 = sortednode.next
            if (l1 is None): sortednode.next = l2
            if (l2 is None): sortednode.next = l1
        return new_head
    # correct solution
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            # create a dummynode (sortednode) 
            # here sortednode is pointed to zero
            temp = sortednode = ListNode(0)
            # check whether l1 and l2 is empty
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            # both are present 
            while (l1 and l2):
                # check which has lesser val
                if l1.val < l2.val:
                    # point dummy node next to lower value
                    sortednode.next = l1
                    l1 = l1.next
                else:
                    sortednode.next = l2
                    l2 = l2.next
                sortednode = sortednode.next
                # if the length of l1 and l2 are not equal
            if (l1):
                sortednode.next = l1
            if (l2):
                sortednode.next = l2
                # since the final output in the sortednode will be 0->resp sorted list
            # so we need to return next val from 0
            return temp.next


if __name__ == "__main__":
    lists = Solution()
    new = ListNode
    new.ListNode()
    #l1 = 1->2->4
    #l2 = 1->3->4
    merge = lists.mergeTwoLists(l1,l2)

