"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        visited = [False]
        
        while stack:
            node, v = stack.pop(), visited.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visited.append(True)
                    for c in node.children[::-1]:
                        stack.append(c)
                        visited.append(False)
        return res