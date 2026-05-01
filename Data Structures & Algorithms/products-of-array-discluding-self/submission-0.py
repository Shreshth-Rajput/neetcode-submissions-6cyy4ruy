class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        running_prod = 1
        for i in range(n):
            res[i] = running_prod
            running_prod *= nums[i]
        running_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= running_prod
            running_prod *= nums[i]

        return res