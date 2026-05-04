import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums[i] = 1
        # We want to find the product of all the elements in nums except for nums[i] = 1
        # So that is going to be 2, 3, 4 (using example 1)

        # 2 * 3 * 4 = 24 -> first ouput

        # Then we move onto nums[i] = 2
        # 1 * 3 * 4 = 12

        # Then nums[i] = 3
        # 1 * 2 * 4 = 8

        # Then nums[i] = 4
        # 1 * 2 * 3 = 6


        # [1, 2, 3 ,4]

        # Iteration 1 = 2 * 3 * 4, output = [24]
        # Iteration 2 =  3 * 4, output = [24, 12]
        # Iteration 3 = 4 * 1 = 4

        
        prefix = [1] * len(nums) 
        
        

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]


        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]


        output = []

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output
             
        
        
       
        

        