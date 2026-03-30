class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter = counter + 1
                max_con = max(max_con, counter)
            else:
                counter = 0
        return max_con