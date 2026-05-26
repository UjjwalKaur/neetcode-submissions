class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate product of all nums
        # divide by the original number
        # if current element = 0, make i = 1

        results = []

        prefix_prod = 1
        for i in range(len(nums)):
            if i > 0:
                prefix_prod *= nums[i - 1]
            results.append(prefix_prod)
        
        postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                postfix_prod *= nums[i + 1]
            results[i] = results[i] * postfix_prod

        return results
            
            
        
            
        