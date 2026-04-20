class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {"I" : [0, 1],
                      "V" : [1, 5],
                      "X" : [2, 10],
                      "L" : [3, 50],
                      "C" : [4, 100],
                      "D" : [5, 500],
                      "M" : [6, 1000]}
        total = 0
        for i in range(len(s) - 1):
            if sym_to_val[s[i]][0] < sym_to_val[s[i + 1]][0]:
                total -= sym_to_val[s[i]][1]
            else:
                total += sym_to_val[s[i]][1]
        return total + sym_to_val[s[len(s) - 1]][1]