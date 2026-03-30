class Solution:
    def maxDifference(self, s: str) -> int:
        all_frequency = {}
        for c in s:
            all_frequency[c] = all_frequency.get(c, 0) + 1
        frequencies = list(all_frequency.values())
        max_odd = float('-inf')
        min_even = float('inf')
        for n in frequencies:
            if n % 2 != 0:
                max_odd = max(max_odd, n)
            else:
                min_even = min(min_even, n)
        return max_odd - min_even 