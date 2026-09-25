class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output = []

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        while k != 0:
            most_common_num = max(freq, key=freq.get)
            output.append(most_common_num)
            del freq[most_common_num]
            k -= 1 
        
        return output
        

        

        