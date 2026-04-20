class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {"I" : 1,
                      "V" : 5,
                      "X" : 10,
                      "L" : 50,
                      "C" : 100,
                      "D" : 500,
                      "M" : 1000}
        res = 0
        for i in range(len(s) - 1):
            if sym_to_val[s[i]] < sym_to_val[s[i + 1]]:
                res -= sym_to_val[s[i]]
            else:
                res += sym_to_val[s[i]]
        return res + sym_to_val[s[len(s) - 1]]