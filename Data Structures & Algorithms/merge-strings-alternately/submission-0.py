class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        left = 0
        right = 0

        while left < len(word1) or right < len(word2):
            if left < len(word1):
                new_string += word1[left]
                left += 1
            
            if right < len(word2):
                new_string += word2[right]
                right += 1

        return new_string