# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stack = [[root, targetSum - root.val]]
        cur = root
        ts = targetSum - root.val
        while cur or stack:
            if cur:
                if ts == 0 and not cur.left and not cur.right:
                    return True
                stack.append([cur.right,ts - cur.right.val if cur.right else 0])
                ts = ts - cur.left.val if cur.left else 0
                cur = cur.left
            else:
                cur, ts = stack.pop()
        return False