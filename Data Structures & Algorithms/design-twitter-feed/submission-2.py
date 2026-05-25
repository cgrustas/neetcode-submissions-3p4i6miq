class Twitter:

    def __init__(self):
        self.users = []
        self.tweets = [] # stack? holds (userId, tweetId) or (tweetId, userId)
        # self.tweetCount?
        self.usersToFollowing = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        for tweet in reversed(self.tweets):
            if len(newsFeed) == 10:
                break

            if tweet[0] == userId or tweet[0] in self.usersToFollowing[userId]:
                newsFeed.append(tweet[1]) 
        return newsFeed  

    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersToFollowing[followerId].discard(followeeId)

