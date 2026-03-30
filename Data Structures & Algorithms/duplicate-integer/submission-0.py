class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = list()
        for i in nums:
            if i in no_duplicates:
                return True
            else:
                no_duplicates.append(i)
        return False