class Solution:
    def mySqrt(self, x: int) -> int:
        lp, rp = 1, x
        while lp <= rp:
            val = (lp + rp) // 2
            val_sq = val * val
            if val_sq == x:
                return val
            elif val_sq > x:
                rp = val - 1
            else:
                lp = val + 1
        return rp