class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        res = []
        while k:
            max_count = max(count_nums.values())
            for count in count_nums:
                if count_nums[count] == max_count:
                    count_nums[count] = float('-inf')
                    res.append(count) 
                    break
            k -= 1
        return res