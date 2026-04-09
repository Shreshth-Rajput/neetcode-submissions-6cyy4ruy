# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rs = 0
        cur = root
        stack = []
        while cur or stack:
            if cur:
                if cur.val in range(low, high + 1):
                    rs += cur.val
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

        return rs