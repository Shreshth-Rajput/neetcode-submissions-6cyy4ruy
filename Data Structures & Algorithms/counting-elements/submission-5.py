class Solution:
    def countElements(self, arr: List[int]) -> int:
        numplus1 = set(arr)
        res = 0
        for num in arr:
            res += 1 if num + 1 in numplus1 else 0
        return res