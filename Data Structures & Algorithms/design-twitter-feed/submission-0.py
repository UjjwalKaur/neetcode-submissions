class Twitter:

    def __init__(self):
        # followerMap that stores list of followers
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        # if len(self.tweetMap[userId]) > 10:
        #    self.tweetMap[userId].pop(0)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followerMap[userId].add(userId)
        for followerId in self.followerMap[userId]:
            if followerId in self.tweetMap:
                index = len(self.tweetMap[followerId]) - 1
                count, tweetId = self.tweetMap[followerId][index]
                minHeap.append([count, tweetId, followerId, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        
