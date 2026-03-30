class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if not len(s) == len(pattern):
            return False
        s_to_p = {}
        p_to_s = {}
        for p, ch in zip(pattern, s):
            if ch in s_to_p and s_to_p[ch] != p:
                return False
            if p in p_to_s and p_to_s[p] != ch:
                return False
            s_to_p[ch] = p
            p_to_s[p] = ch
        return True