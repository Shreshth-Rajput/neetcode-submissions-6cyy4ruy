class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            if num in mapping:
                return [mapping[num], i]
            mapping[target - num] = i
