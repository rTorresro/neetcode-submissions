class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first-second))
            
        if not heap:
            return 0

        
        return -heap[0]

        
        