class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # to peek at the top element, just get the element at the 0th index
        if (self.small and self.large and self.large[0] < (-1 * self.small[0])):
            extra = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, extra)
        if (len(self.small) - len(self.large) > 1):
            extra = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, extra)
        elif (len(self.large) - len(self.small) > 1):
            extra = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * extra)


    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return ((-1 * self.small[0]) + self.large[0]) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -1 * self.small[0]
        
        