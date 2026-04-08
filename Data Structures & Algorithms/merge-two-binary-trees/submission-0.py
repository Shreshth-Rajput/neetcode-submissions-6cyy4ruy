# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def helper(cur1, cur2):
            if not cur1 and not cur2:
                return None

            node = TreeNode((cur1.val if cur1 else 0) + (cur2.val if cur2 else 0))
            node.left = helper(cur1.left if cur1 else None, cur2.left if cur2 else None)
            node.right = helper(cur1.right if cur1 else None, cur2.right if cur2 else None)

            return node

        return helper(root1, root2)