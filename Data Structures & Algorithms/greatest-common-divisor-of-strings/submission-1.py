class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        divi = ""
        for i in range(min(len(str1), len(str2))):
            divi += str2[i]
            if not len(str1) % len(divi) and not len(str2) % len(divi):
                f1, f2 = len(str1) // len(divi), len(str2) // len(divi)
                if divi * f1 == str1 and divi * f2 == str2:
                    res = divi
        return res