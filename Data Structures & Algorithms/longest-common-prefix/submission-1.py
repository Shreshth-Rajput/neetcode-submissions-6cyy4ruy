class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            pos_pre = strs[0][i] 
            for s in strs:
                try:
                    if not s[i] == pos_pre:
                        return prefix
                except IndexError:
                    return prefix
            else:
                prefix += pos_pre
        return prefix
            