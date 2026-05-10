class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for i in nums:
            # Only start counting if i is the beginning of a sequence
            if i - 1 not in num_set:
                current = i
                length = 1

                # Extend the sequence as far as it goes
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest