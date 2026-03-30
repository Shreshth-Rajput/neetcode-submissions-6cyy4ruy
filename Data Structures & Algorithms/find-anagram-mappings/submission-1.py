class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        index_lookup = dict() 
        for j, num2 in enumerate(nums2):
            index_lookup[num2] = j
        for i, num1 in enumerate(nums1):
            res[i] = index_lookup[num1]
        return res