import praw
import creds as r


class REDDIT():
    """
    """
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=r.client_id,
            client_secret=r.client_secret,
            username=r.username,
            password=r.password,
            user_agent=r.user_agent
        )

    def getImages(self, sub, number):
        retArray = []
        for submission in reddit.subreddit('sub').hot(limit=number):
            retArray.append(submission)
        return retArray

if __name__ == '__main__':
    redd = REDDIT()

    
