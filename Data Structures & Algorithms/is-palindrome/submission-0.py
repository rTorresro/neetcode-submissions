class Solution:
    def isPalindrome(self, s: str) -> bool:

        check = []

        for char in s:
            if char.isalnum():
                check.append(char.lower())

        if not check:
            return True 


         
        left = 0
        right = len(check) - 1

        while left < right:
            if check[left] == check[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True 
            


            

        
         
            
       

        