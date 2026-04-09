# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(cur, rs):
            if cur:
                if cur.val in range(low, high + 1):
                    rs += cur.val
                rs = helper(cur.left, rs)
                rs = helper(cur.right, rs)
            return rs
        

        return helper(root, 0)