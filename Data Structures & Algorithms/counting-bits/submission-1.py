class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            k = i
            while k:
                res[i] += k % 2
                k = k >> 1
        return res
