class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use a hash map
        freq = {}
        for i in range (len(nums) + 1):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] >= 2:
                return nums[i]

        return -1
        