import heapq
class Twitter:

    def __init__(self):
        self.posts=dict()
        self.follows=dict()
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId]=[[self.count, tweetId]]
            self.follows[userId]=[userId]
            self.count+=1
        else:
            self.posts[userId].append([self.count, tweetId])
            self.count+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows:
            self.follows[userId]=[userId]
            self.posts[userId]=[]
        followings=self.follows[userId]
        max_heap_tweets=list()
        for f in followings:
            max_heap_tweets.extend(self.posts[f])
        for i in range(len(max_heap_tweets)):
            max_heap_tweets[i]=[-max_heap_tweets[i][0], max_heap_tweets[i][1]]
        heapq.heapify(max_heap_tweets)
        res=list()
        for i in range(10):
            if len(max_heap_tweets)>0:
                res.append(heapq.heappop(max_heap_tweets)[1])
            else:
                break
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId]=[followerId]
            self.posts[followerId]=[]
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId]=[followerId]
            self.posts[followerId]=[]
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
