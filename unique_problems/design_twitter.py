class Twitter:
    def __init__(self):
        self.follow_dict = {}
        self.tweet_stack = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follow_dict:
            self.follow_dict[userId] = set()
        self.tweet_stack.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        for i in range(len(self.tweet_stack) - 1, -1, -1):
            if len(ans) == 10:
                break
            tweet = self.tweet_stack[i]
            if tweet[0] == userId or tweet[0] in self.follow_dict[userId]:
                ans.append(tweet[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_dict:
            self.follow_dict[followerId].add(followeeId)
        else:
            self.follow_dict[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId in self.follow_dict
            and followeeId in self.follow_dict[followerId]
        ):
            self.follow_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
