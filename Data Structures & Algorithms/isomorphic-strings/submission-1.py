class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapped = {}
        if not len(s) == len(t):
            return False
        for i in range(len(s)):
                if s[i] in mapped:
                    if not mapped[s[i]] == t[i]:
                        return False
                elif t[i] in mapped.values():
                    return False
                else:
                    mapped[s[i]] = t[i]
        return True