class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        cur = self.root
        for c1, c2 in zip(w, reversed(w)):
            if not (c1, c2) in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1
        
    def count(self, w):
        cur = self.root
        for c1, c2 in zip(w, reversed(w)):
            if not (c1, c2) in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for w in reversed(words):
            res += trie.count(w)
            trie.add(w)
        return res