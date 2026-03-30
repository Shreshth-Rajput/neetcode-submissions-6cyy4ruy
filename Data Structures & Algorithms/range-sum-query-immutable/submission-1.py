class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = list()
        cur = 0
        for n in nums:
            cur += n
            self.sums.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)