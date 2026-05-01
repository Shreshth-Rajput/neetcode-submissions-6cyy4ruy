class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] = 1
        res = 0
        cur_sum = 0
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += pre_sum[diff]
            pre_sum[cur_sum] += 1
        return res