class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = list()
        for num in nums:
            nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * (-1)
        for i, num in enumerate(nums):
            if num == abs(num):
                output.append(i + 1)
        return output