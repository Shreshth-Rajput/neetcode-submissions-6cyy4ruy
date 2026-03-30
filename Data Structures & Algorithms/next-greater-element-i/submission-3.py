class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = list()
        for i in nums1:
            nums2_index = nums2.index(i)
            for n2 in range(nums2_index + 1, len(nums2)):
                if nums2[n2] > i:
                    output.append(nums2[n2])
                    break
            else:
                output.append(-1)
        return output