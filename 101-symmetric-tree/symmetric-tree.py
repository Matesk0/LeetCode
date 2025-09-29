# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mirror(self, left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            return left.val == right.val and mirror(self, left.left, right.right) and mirror(self, left.right, right.left)

        if not root:
            return True
        
        return mirror(self, root.left, root.right)