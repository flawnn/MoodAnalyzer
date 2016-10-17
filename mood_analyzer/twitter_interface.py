from loklak import Loklak
import datetime


def get_tweets(hashtag, since=0, count=100):
    """
    Fetches all tweets to a given hashtag
    :param hashtag: (str) keyword
    :param since: (str) Y-M-D
    :param count: (int) count
    :return: (list, int, int) 1. Content, 2.
    """

    l = Loklak()
    since = datetime.datetime.now() + datetime.timedelta(days=-since)
    since = datetime.datetime.strftime(since, "%Y-%m-%d")
    tweet_list = []
    for t in l.search(hashtag, since=since, count=count)["statuses"]:
        tweet_list.append(t["text"])

    return tweet_list #, len(tweet_list), since


if __name__ == "__main__":
    print(get_tweets(('trump')))
