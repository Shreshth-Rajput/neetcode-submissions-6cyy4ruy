class PrefixNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def add(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
            cur.count += 1


    def ret_count(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()
        for w in words:
            prefix_tree.add(w)
        return prefix_tree.ret_count(pref)