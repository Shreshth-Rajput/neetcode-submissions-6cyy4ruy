class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = {"b" : 0, "a" : 0,"n" : 0}
        double_balloons = {"l" : 0, "o" : 0}
        for ch in text:
            if ch in balloons:
                balloons[ch] += 1
            elif ch in double_balloons:
                double_balloons[ch] += 0.5
    
        print(balloons, double_balloons)
        min_double = min(list(double_balloons.values()))
        min_single = min(list(balloons.values())) 
        return math.floor(min(min_double, min_single))