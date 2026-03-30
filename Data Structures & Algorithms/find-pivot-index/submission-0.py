class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                right_sum += nums[j]
            else:
                if right_sum == left_sum:
                    return i
            right_sum = 0
            left_sum += nums[i]
        return -1