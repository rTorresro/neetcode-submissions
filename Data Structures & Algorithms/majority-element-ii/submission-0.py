class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:


        freq = {}
        new_list = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for val in freq:
            if freq[val] > (len(nums) / 3):
                new_list.append(val)
        
        return new_list



        