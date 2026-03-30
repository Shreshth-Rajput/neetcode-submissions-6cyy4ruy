class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        inc_subarray = [nums[0]]
        cur_sum = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_subarray.append(nums[i])
            else:
                cur_sum = sum(inc_subarray)
                inc_subarray.clear()
                inc_subarray.append(nums[i])
            if i == len(nums) - 1:
                cur_sum = sum(inc_subarray)
            max_sum = max(cur_sum, max_sum)
        return max_sum