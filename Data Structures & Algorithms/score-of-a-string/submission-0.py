class Solution:
    def scoreOfString(self, s: str) -> int:
        total_ascii = 0
        for i in range(len(s) - 1):
            total_ascii = total_ascii + abs((ord(s[i]) - ord(s[i+1])))
        return total_ascii