class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a minHeap of n - k + 1 elements
        # Then the largest is the k-th largest or the last element popped when removing excess

        heapq.heapify(nums)
        i = len(nums) - k + 1

        while i > 0:
            popped = heapq.heappop(nums)
            i -= 1

        return popped
        