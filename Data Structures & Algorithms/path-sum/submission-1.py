# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(cur_sum, cur):

            if not cur:
                return False

            cur_sum += cur.val

            if not cur.left and not cur.right:
                return cur_sum == targetSum
            
            return (dfs(cur_sum, cur.left) or dfs(cur_sum, cur.right))

        return dfs(0, root)