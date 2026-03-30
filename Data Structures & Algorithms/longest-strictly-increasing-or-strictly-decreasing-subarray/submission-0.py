class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur_count = 1
        max_count = 1
        prev_increasing = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if prev_increasing > 0:
                    cur_count += 1
                else:
                    cur_count = 2
                    prev_increasing = 1
            elif nums[i] < nums[i-1]:
                if prev_increasing < 0:
                    cur_count += 1
                else:
                    cur_count = 2
                    prev_increasing = -1
            else:
                cur_count = 1
                prev_increasing = 0
            max_count = max(cur_count, max_count)
        return max_count