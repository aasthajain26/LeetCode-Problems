# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
 

        def maxDepth1(root):
            
            if root is None:
                return 0
            else:
                l=maxDepth1(root.left)
                r=maxDepth1(root.right)
                m = max(l,r)
            return m+1


        m =maxDepth1(root)
        return m