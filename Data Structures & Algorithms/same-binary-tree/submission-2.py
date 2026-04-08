# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur_p, cur_q = p, q
        stack_p, stack_q = [cur_p], [cur_q]
        while (cur_p or stack_p) and (cur_q or stack_q):
            if cur_p and cur_q:
                if not cur_p.val == cur_q.val:
                    return False
                stack_p.append(cur_p.right)
                stack_q.append(cur_q.right)
                cur_p = cur_p.left
                cur_q = cur_q.left
            elif cur_p and not cur_q:
                return False
            elif cur_q and not cur_p:
                return False
            else:
                cur_p = stack_p.pop()
                cur_q = stack_q.pop()
        
        print("true??")
        return len(stack_p) == len(stack_q) == 0