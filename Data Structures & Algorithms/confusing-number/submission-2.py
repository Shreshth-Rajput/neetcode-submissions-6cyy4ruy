class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_mapping = {0 : 0, 1 : 1, 6 : 9, 8 : 8, 9 : 6}
        n_copy = n
        rotated = 0
        while n_copy:
            cur_digit = n_copy % 10
            if cur_digit in rotation_mapping:
                rotated = rotated * 10 + rotation_mapping[cur_digit]
            else:
                return False
            n_copy = n_copy // 10
        return not rotated == n
