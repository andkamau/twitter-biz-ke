import tweepy, os
creds = os.getenv('TWITTER_API_CREDENTIALS').split(',')
auth = tweepy.OAuthHandler(creds[0], creds[1])
auth.set_access_token(creds[2], creds[3])
api = tweepy.API(auth)
api.get_status('748567826907136000')
