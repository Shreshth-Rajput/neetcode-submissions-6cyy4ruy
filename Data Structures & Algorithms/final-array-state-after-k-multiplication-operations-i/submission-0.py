class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        
        while k:
            n, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))
            k -= 1

        return nums