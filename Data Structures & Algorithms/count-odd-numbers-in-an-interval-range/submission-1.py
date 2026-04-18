class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (1 if low % 2 == 1 else 0) + (1 if high % 2 == 1 else 0)
        count += (high - low - 1) // 2
        return max(count, 0)