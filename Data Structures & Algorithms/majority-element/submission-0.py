class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # add each num in nums to a hash map
        # the key with the highest value will get returned

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return max(freq, key=freq.get)


        