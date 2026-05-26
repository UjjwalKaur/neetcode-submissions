class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0

        for num in numset:
            if not (num - 1 in numset):
                length = 0
                while (num+length in numset):
                    length += 1
                longest = max(length, longest)

        return longest
        