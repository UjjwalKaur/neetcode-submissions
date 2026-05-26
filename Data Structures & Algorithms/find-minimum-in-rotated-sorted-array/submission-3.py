class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the only pair that yields a negative result when
        # the second element is subtracted from the first element

        # binary search 
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2 
            if (mid + 1 < len(nums) and nums[mid + 1] - nums[mid] < 0):
                return nums[mid + 1]
            if (nums[mid] > nums[end]):
                start = mid + 1
            else:
                end = mid

        return nums[start]
            
        

        