class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def get_val(i: int, start: int):
            return (start + i) % len(nums)
        
        start = 0 
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        # start is now the start of the ascending pattern in the array
        # normal binary search with modified arrays
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if (nums[get_val(mid, start)] == target):
                return get_val(mid, start)
            elif (nums[get_val(mid, start)] < target):
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
