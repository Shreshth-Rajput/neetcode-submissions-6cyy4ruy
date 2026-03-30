class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) / 2
        seen = list()
        for i in range(len(nums)):
            if not nums[i] in seen:
                if nums.count(nums[i]) > majority_count:
                    return nums[i]
                else:
                    seen.append(nums[i])
