from loklak import Loklak

loklak = Loklak()
def get_tweets(hashtag):
    """
    Fetches all tweets to a given hashtag
    :param hashtag: (str) keyword
    :return: (list) list of json strings with content
    """
    tweet_list = []

    for t in loklak.search(hashtag)["statuses"]:
        tweet_list.append(t["text"])

    return tweet_list

def get_status(self): 

    print(loklak.status())


if __name__ == "__main__":
    for tweet in get_tweets('jugendhackt'):
        print(tweet)
