# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import queue
        res = []
        q = queue.Queue()
        if root is None:
            return None
        q.put(root)
        while not q.empty():
            a = []
            size = q.qsize()
            while size != 0:
                curr = q.get()
                a.append(curr.val)
                if curr.left is not None:
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)
                size -= 1
            if len(a) !=0:
                print(a)
                res.append(a)
        return res 
