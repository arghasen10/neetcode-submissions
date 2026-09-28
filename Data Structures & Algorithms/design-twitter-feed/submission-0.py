import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for user in self.following[userId] | {userId}:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweet_id = self.tweets[user][index]
                heapq.heappush(heap, (-time,tweet_id, user, index))
            
        feed = []

        while heap and len(feed) < 10:
            _, tweet_id, user, index = heapq.heappop(heap)
            feed.append(tweet_id)

            if index > 0:
                index-=1
                time,next_id=self.tweets[user][index]
                heapq.heappush(heap,(-time, next_id, user, index))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
