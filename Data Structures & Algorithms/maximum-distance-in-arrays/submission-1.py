class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        maxs = arrays[0][-1]
        mins = arrays[0][0]
        res = float("-inf")
        
        for i in range(1, n):
            res = max(res, abs(maxs - arrays[i][0]), abs(arrays[i][-1] - mins))
            maxs = max(maxs, arrays[i][-1])
            mins = min(mins, arrays[i][0]) 


        return res