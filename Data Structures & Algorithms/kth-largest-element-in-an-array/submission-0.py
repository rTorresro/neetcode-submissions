class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

    
        # add all elements in the list to a heap

        heap = []

        for i in nums:
            heapq.heappush(heap, -i)

         
        # pop k amount of times to get kth largest number

        while k != 0:
            kth_largest = -heapq.heappop(heap) 
            k -= 1
        
        return kth_largest

    

        
        