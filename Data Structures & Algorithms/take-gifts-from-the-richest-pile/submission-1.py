class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)
        while k:
            heapq.heappush(gifts, int(-sqrt(-heapq.heappop(gifts))))
            k -= 1

        return -sum(gifts)