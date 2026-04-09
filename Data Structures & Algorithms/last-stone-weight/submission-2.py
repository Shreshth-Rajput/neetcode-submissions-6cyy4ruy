class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:

            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if not x == y:
                heapq.heappush(heap, -abs(x - y))
        
        return -heapq.heappop(heap) if heap else 0