class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        outbit = [0] * (n + 1)
        output = list()
        for num in nums:
            outbit[num] += 1
        for i, ob in enumerate(outbit):
            if i == 0:
                continue
            if ob == 0:
                output.append(i)
        return output