from loklak import Loklak
import datetime


loklak = Loklak()
def get_tweets(hashtag, since=14, count=500):
    """
    Fetches all tweets to a given hashtag
    :param hashtag: (str) keyword
    :param since: (str) Y-M-D
    :param count: (int) count
    :return: (list) list of json strings with content
    """
    now = datetime.datetime.now()
    since = now + datetime.timedelta(days=-since)
    since = datetime.datetime.strftime(since, "%Y-%m-%d")
    print(since)
    tweet_list = []

    for t in loklak.search(hashtag, since=since, count=count)["statuses"]:
        """Parameters: self, query=None, since=None, until=None, from_user=None, count=None """
        tweet_list.append(t["text"])

    return tweet_list, len(tweet_list), since


if __name__ == "__main__":
    counter = 0
    for tweets in get_tweets("Trump"):
        counter += 1
        print(tweets, counter, )


