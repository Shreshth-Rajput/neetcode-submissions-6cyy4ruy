class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = 0
        while True:
            if n == 0:
                if total == 1:
                    return True

                n = total                
                if total in seen:
                    return False
                else:
                    seen.add(total)
                total = 0

            digit = n % 10
            n = n // 10
            total = digit ** 2 + total
