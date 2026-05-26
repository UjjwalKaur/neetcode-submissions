class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        result = []

        for i, num in enumerate(nums):
            if ((target - num) in dict.keys()):
                result.append(dict[target - num])
                result.append(i)
                return result
            else:
                dict[num] = i

        