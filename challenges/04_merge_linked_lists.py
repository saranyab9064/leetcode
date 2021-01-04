# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # initialise two pointers
        p1 = l1
        p2 = l2
        head=p3 = ListNode(0)

        while True:
            if p1 is None: 
                p3.next = p2 
                break
            if p2 is None: 
                p3.next = p1 
                break

            if p1.val >= p2.val:
                p3.next = p2
                p2 = p2.next
            else: 
                p3.next = p1
                p1 = p1.next
        
            p3 = p3.next
        return(head.next)



def print_recursive(l):
    if l is None:
        return ''
    return str(l.val) + '->' + print_recursive(l.next)

    
if __name__ == "__main__":
    l1 = Solution()
    l2 = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    print(print_recursive(l1))

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    print(print_recursive(l2))
    test = Solution()
    l3 =  test.mergeTwoLists(l1,l2)
    print(print_recursive(l3))
