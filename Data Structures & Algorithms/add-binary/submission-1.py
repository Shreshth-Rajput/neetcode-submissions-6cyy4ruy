class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            total = (int(a[i]) if i < len(a) else 0) + (int(b[i]) if i < len(b) else 0) + carry
            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = "1" + res
        
        return res