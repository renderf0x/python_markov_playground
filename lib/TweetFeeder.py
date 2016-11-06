import requests

class TweetFeeder:
    account = None
    auth = None
    access_token = None

    def __init__(self, account, auth):
        self.account = account
        self.auth = auth

    def fetch(self, number_to_fetch = 20):
        self._get_access_token()
        tweets = self._get_tweet_texts(number_to_fetch)
        return tweets

    # helpers
    def _get_access_token(self):
        authHeader = 'Basic ' + self.auth
        url = 'https://api.twitter.com/oauth2/token'
        headers = {'Authorization': authHeader, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8.' }
        payload = {'grant_type' : 'client_credentials'}

        r = requests.post(url, headers=headers, data=payload)
        response_json = r.json()
        self.access_token = response_json['access_token']

    def _get_tweets(self, number):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + self.account + "&count=" + str(number)
        authHeader = "Bearer " + self.access_token
        headers = { "Authorization" : authHeader }
        r = requests.get(url, headers=headers)

        response_json = r.json()
        return response_json

    def _get_tweet_texts(self, numtweets):
        tweets = self._get_tweets(numtweets)
        response_texts = []

        for i in range(0, len(tweets)):
            response_texts.append(tweets[i]['text'])
        return response_texts
