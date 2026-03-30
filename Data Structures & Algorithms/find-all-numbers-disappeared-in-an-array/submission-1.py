class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        outbit = [False] * (n + 1)
        output = list()
        for num in nums:
            outbit[num] = True
        for i, ob in enumerate(outbit):
            if i == 0:
                continue
            if ob == False:
                output.append(i)
        return output