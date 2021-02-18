# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def recursive(root):
            if not root:
                return 
            recursive(root.left)
            res.append(root.val)
            recursive(root.right)
        recursive(root)
        return res
