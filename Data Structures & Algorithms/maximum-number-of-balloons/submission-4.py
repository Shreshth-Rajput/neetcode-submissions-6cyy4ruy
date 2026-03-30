class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = {"b" : 0, "a" : 0,"n" : 0, "l" : 0, "o" : 0}
        for ch in text:
            if ch in ["l", "o"]:
                balloons[ch] += 0.5
            elif ch in ["b", "a", "n"]:
                balloons[ch] += 1
        
        return math.floor(min(balloons.values()))
