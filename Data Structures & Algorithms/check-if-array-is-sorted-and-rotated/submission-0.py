class Solution:
    def check(self, nums: List[int]) -> bool:
        og_len = len(nums)
        len_matches = 1
        nums = nums * 2
        for i in range(len(nums) - 1):
            if nums[i + 1] >= nums[i]:
                len_matches += 1
            else:
                len_matches = 1
            if len_matches == og_len:
                return True
        return False