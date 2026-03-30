class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated = {0 : 0, 1 : 1, 6 : 9, 8 : 8, 9 : 6}
        inverted = 0
        n_copy = n
        while n_copy > 0:
            digit = n_copy % 10
            if not digit in rotated:
                return False
            inverted = inverted * 10 + rotated[digit]
            n_copy = n_copy // 10
        return not inverted == n