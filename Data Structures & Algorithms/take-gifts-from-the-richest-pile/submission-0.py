class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)
        while k:
            pile = heapq.heappop(gifts)
            heapq.heappush(gifts, int(-sqrt(-pile)))
            k -= 1

        return -sum(gifts)