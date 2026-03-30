class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        count_balloon = Counter("balloon")
        min_balloons = float('inf')
        for ch in count_balloon:
            min_balloons = min(min_balloons, count_text[ch] // count_balloon[ch])
        return min_balloons