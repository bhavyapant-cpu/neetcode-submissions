class Twitter:

    def __init__(self):
        self.lastIndex=0
        self.userDict={}
        self.userPost={}  

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.tweetArray.append(tweetId)
        if userId not in self.userDict:
            self.userDict[userId]=[userId]
        if userId not in self.userPost:
            self.userPost[userId]=[]
        
        self.userPost[userId].append([-(self.lastIndex),tweetId])
        self.lastIndex+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        queue=[]
        for followeeId in self.userDict[userId]:
            if followeeId in self.userPost:
                length=len(self.userPost[followeeId])
                x=length-10 if length>10 else 0
                for tweet in range(x,length):
                    y=self.userPost[followeeId][tweet]
                    heapq.heappush(queue,y)
            
        tweets=[]
        for i in range(0,10):
            if not queue:
                break
            tweets.append(heapq.heappop(queue)[1])
        return tweets    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userDict:
            self.userDict[followerId]=[followerId]
        if followeeId not in self.userDict[followerId]:
            self.userDict[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         if followeeId in self.userDict[followerId] and followeeId != followerId:
            self.userDict[followerId].remove(followeeId)
        
