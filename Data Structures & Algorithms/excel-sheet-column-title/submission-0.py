class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            res += chr(ord("A") + digit)
            columnNumber = (columnNumber - 1) // 26
        
        return res[::-1]