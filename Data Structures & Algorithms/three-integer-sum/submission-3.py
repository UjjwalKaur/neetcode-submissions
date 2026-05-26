class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # how to choose the third pointer in the most efficient way
        nums.sort()
        start = 0
        end = len(nums) - 1
        mid = nums[0]
        result = []

        for i, num in enumerate(nums):
            # skip this iteration if curr element is the same as prev element 
            # this condition should only be checked if i > 0
            # this needs to be done before start and end values are assigned!
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            start = i + 1 # num at index i is already one of the three numbers being added
            end = len(nums) - 1

            while start < end:
                sum = nums[start] + num + nums[end]
                
                if (sum == 0):
                    result.append([num, nums[start], nums[end]])
                    # make sure to move the pointers after appending to the array
                    start = start + 1
                    end = end - 1
                    # skip if the next element is the same as the prev element
                    while (start < end and nums[start] == nums[start - 1]):
                        start = start + 1
                elif (sum > 0):
                    end = end - 1
                elif (sum < 0):
                    start = start + 1

        return result
        