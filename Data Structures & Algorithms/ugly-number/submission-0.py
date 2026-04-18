class Solution:
    def isUgly(self, n: int) -> bool:
        p_fact = [2, 3, 5]
        while True:
            if not n % 5:
                n = n // 5
            elif not n % 3:
                n = n // 3
            elif not n % 2:
                n = n // 2
            elif n == 1:
                return True
            else:
                return False
            