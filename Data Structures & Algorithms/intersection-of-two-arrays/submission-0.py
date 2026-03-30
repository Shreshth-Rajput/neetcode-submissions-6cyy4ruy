class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set_nums2 = set(nums2)
        for n in nums1:
            if n in set_nums2:
                res.add(n)
        return list(res)