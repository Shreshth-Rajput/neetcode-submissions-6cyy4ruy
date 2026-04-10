class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        return "1" * (count["1"] - 1) + "0" * count["0"] + "1"