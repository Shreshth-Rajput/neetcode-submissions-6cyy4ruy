class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_colours = Counter(nums)
        cur_colour = 0
        for i in range(len(nums)):
            while not count_colours[cur_colour]:
                cur_colour += 1
            nums[i] = cur_colour
            count_colours[cur_colour] -= 1
            if cur_colour > 2:
                break
                
                
