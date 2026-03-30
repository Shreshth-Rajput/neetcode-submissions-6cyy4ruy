class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = float("-inf")
        for i in range(len(num)):
            if len(num[i:i+3]) < 3:
                break
            if (int(num[i:i+3]) % 111 == 0):
                res = max(res, int(num[i:i+3]))
        if res == 0:
            return "000"
        elif not res == float("-inf"):
            return str(res)
        return ""