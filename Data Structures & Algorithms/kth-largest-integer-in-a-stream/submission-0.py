class KthLargest:

    def __init__(self, k: int, nums: list[int]):

        self.k = k
        self.heap = []

        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]
        
