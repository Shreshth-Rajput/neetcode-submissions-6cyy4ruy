class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lp, rp = 1, num // 2
        if num == 1:
            return True
        while lp <= rp:
            val = (lp + rp) // 2
            val_sq = val * val
            if val_sq == num:
                return True
            elif val_sq > num:
                rp = val - 1
            else:
                lp = val + 1
        return False