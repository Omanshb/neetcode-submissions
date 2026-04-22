class Twitter:

    def __init__(self):
        self.hp = []
        self.following = {}
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter -= 1
        heapq.heappush(self.hp, (self.counter, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.following, self.hp)
        lst = []
        hold = []
        while self.hp and len(lst) < 10:
            curr = heapq.heappop(self.hp)
            if curr[1] == userId or curr[1] in self.following.get(userId, set()):
                lst.append(curr[2])
            hold.append(curr)

        for tweet in hold:
            heapq.heappush(self.hp, tweet)
        
        return lst
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId, set()):
            self.following[followerId].remove(followeeId)
        
