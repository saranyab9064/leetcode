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

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      head = ListNode(0)
      ptr = head
      while True:
          if l1 is None and l2 is None:
              break
          elif l1 is None:
              ptr.next = l2
          elif l2 is None:
              ptr.next = l1
              break
          else:
              smallest_val = 0
              if l1.val <= l2.val:
                  smallest_val = l1.val
                  l1 = l1.next
              else:
                  smallest_val = l2.val
                  l2 = l2.next
              newNode = ListNode(smallest_val)
              ptr.next = newNode
              ptr = ptr.next
      return head.next

if __name__ == "__main__":
    lists = Solution()
    new = ListNode
    new.ListNode()
    merge = lists.mergeTwoLists(l1,l2)

