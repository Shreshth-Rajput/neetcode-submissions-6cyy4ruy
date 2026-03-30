class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_left_shift = 0
        for shift_dir, shift_by in shift:
            total_left_shift += shift_by if shift_dir == 0 else -shift_by
        total_left_shift %= len(s)
        return s[total_left_shift:] + s[:total_left_shift]