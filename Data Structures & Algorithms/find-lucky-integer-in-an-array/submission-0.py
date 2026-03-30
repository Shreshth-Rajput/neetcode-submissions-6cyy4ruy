class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_arr = Counter(arr)
        lucky = -1
        for n in count_arr:
            if count_arr[n] == n:
                lucky = max(lucky, n)
        return lucky