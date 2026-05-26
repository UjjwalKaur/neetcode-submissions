class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hash map = {frequency : number}
        # hash map = {number : frequency}

        nums.sort()

        dict = {}
        results = []

        for num in nums:
            # useful trick to make getting and updating a value in both cases easy:
            # case 1: dict[num] exists
            # case 2: dict[num] does not exist
            dict[num] = 1 + dict.get(num, 0)

        # next, we must do bucket sort such that, 
        # freq = [all numbers that have that frequency]

        buckets = [[] for i in range(len(nums) + 1)]
        # + 1 because the maximum frequency can be len(nums)
        # but the range function does not include the last element

        for key, val in dict.items():
            buckets[val].append(key)

        # iterating in reverse order
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                results.append(n)
                if (len(results) == k):
                    return results  