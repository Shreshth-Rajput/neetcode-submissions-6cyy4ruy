class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n):
            tmp = one + two
            two = one
            one = tmp
        return two