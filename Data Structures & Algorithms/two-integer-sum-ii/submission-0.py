class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        left = 0
        right = len(numbers) - 1 

        while (left < right):

            # if the numbers all the way to the right and left already equal target, return the indexes of those numbers 
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
            

            
        
            

            
            
            
                

        