class Solution:
    def check(self, nums: List[int]) -> bool:
        og_len = len(nums)
        len_matches = 1
        for i in range(1, og_len * 2):
            if nums[(i - 1) % og_len] <= nums[i % og_len]:
                len_matches += 1
            else:
                len_matches = 1
            if len_matches == og_len:
                return True
        return False