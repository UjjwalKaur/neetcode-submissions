class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate product of all nums
        # divide by the original number
        # if current element = 0, make i = 1

        product = 1
        zero = 0

        for num in nums:
            if num == 0:
                num = 1
                zero += 1

            product *= num

        results = []
        for num in nums:
            if zero == 1:
                if num == 0:
                    results.append(product)
                else:
                    results.append(0)
            elif (zero == 0):
                results.append(product // num)
            else:
                results.append(0)

        return results
            
            
        
            
        