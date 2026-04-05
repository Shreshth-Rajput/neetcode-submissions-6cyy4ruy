# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lp, rp = 1, n
        while lp <= rp:
            idx = (lp + rp) // 2
            res = guess(idx)
            if res == 0:
                return idx
            elif res == -1:
                rp = idx - 1
            else:
                lp = idx + 1