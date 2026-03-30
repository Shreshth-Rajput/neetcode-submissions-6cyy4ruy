class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        n = len(nums)
        res = []
        bucket = [[] for _ in range(n)] 
        for num in count_nums:
            print(count_nums[num])
            bucket[count_nums[num] - 1].append(num)
        for num_list in reversed(bucket):
            for num in num_list:
                res.append(num)
                k -= 1
                if k == 0:
                    return res