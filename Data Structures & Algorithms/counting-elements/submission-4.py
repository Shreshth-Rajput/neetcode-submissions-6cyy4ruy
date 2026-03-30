class Solution:
    def countElements(self, arr: List[int]) -> int:
        numcount = Counter(arr)
        res = 0
        for num in arr:
            res += 1 if num + 1 in numcount else 0
        return res