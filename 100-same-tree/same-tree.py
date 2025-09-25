# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def check(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None or \
                p.val != q.val:
                return False
            
            if check(p.left, q.left) and check(p.right, q.right):
                return True
            
            return False
        
        return check(p, q)



        