class Solution:
    def arrangeCoins(self, n: int) -> int:
        lp, rp = 1, n
        res = lp
        while lp <= rp:
            k = (lp + rp) // 2
            gauss = (k/2) * (k + 1)
            if gauss > n:
                rp = k - 1
            elif gauss < n:
                res = max(res, k)
                lp = k + 1
            else:
                return res
        return res