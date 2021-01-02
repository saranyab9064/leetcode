
"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = None

    

class Solution(object):


    def addtolist(self,newdata):
        newNode = ListNode(newdata)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

    def length(self):
         cur = self.head
         total = 0
         while cur.next != None:
             total += 1
             cur = cur.next
         return total

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry = 0
        # declare curr_ele variable to help traverse and add nodes to new list
        # declare head variable to be the head of the list
        head = curr_ele= ListNode(0)
      
        while p1 or p2 or carry:
            print(p1.val,p2.val,carry)
            sum_val = carry
            if p1 is None:
                sum_val += 0
            else: sum_val += p1.val
            if p2 is None:
                sum_val += 0
            else: sum_val += p2.val
            
            if sum_val >=10:
                sum_val = sum_val-10
                carry = 1
            else:
                carry = 0
            print(sum_val,carry)
            curr_ele.next = ListNode(sum_val)
            curr_ele = curr_ele.next

            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

            
        return head.next
def print_recursive(l):
    if l is None:
        return ''
    return str(l.val) + '->' + print_recursive(l.next)
if __name__ == "__main__":
    l1 = Solution()
    l2 = Solution()
    ''' 
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(9)
    l1.addtolist(8)
    l1.addtolist(9)

    l2.addtolist(5)
    l2.addtolist(6)
    l2.addtolist(4)
    l1.printList()
    l2.printList() 
    '''
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print(print_recursive(l1))

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(print_recursive(l2))

    test = Solution()
    l3 =  test.addTwoNumbers(l1,l2)
    print(print_recursive(l3))
    



        
