# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        res = [[]]
        level = 0
        self.helper_func(root,level,res)
        return res
        
    def helper_func(self,root,level,res):
        if root is None:
            return None
        
        if len(res)<level+1:
            res.append([])
            
        if level % 2 == 1:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)
            
        self.helper_func(root.right,level+1,res)
        self.helper_func(root.left,level+1,res)
        
