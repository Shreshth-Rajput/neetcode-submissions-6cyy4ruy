class Solution:
    def isUgly(self, n: int) -> bool:
        p_fact = [2, 3, 5]
        for p in p_fact:
            while not n % p:
                n = n // p
        return n == 1
