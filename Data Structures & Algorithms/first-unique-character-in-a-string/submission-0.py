class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = [0] * 26
        for ch in s:
            seen[ord(ch) - ord("a")] += 1
        for i, ch in enumerate(s):
            if seen[ord(ch) - ord("a")] == 1:
                return i
        return -1