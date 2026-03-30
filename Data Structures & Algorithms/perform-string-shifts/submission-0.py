class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        len_s = len(s)
        for shift_dir, shift_by in shift:
            if shift_dir == 0:
                s = s[shift_by:] + s[:shift_by]
            else:
                s = s[len_s - shift_by:] + s[:len_s - shift_by]
        return s