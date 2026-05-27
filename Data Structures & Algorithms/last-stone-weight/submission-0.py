class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python does not have maxHeaps so we convert every int to a negative int
        stones = [-s for s in stones]
        maxHeap = stones
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if second > first:
                heapq.heappush(maxHeap, first - second)

        maxHeap.append(0)
        return abs(maxHeap[0])


        