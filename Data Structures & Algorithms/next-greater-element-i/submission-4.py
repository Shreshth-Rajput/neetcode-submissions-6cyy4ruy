class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        index_mapping = dict()
        stack = list()
        for i, num1 in enumerate(nums1):
            index_mapping[num1] = i
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                res = stack.pop()
                output[index_mapping[res]] = num2
            if num2 in index_mapping:
                stack.append(num2)
        return output
            