class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        res = -1
        for num, occur in count_nums.items():
            if occur == 1:
                res = max(res, num)
        return res