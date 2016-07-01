import os
redis_host = os.getenv('REDIS_HOST', 'localhost:6379')
REDIS = dict(
        host=redis_host.split(':')[0],
        port=redis_host.split(':')[1],
        db='4',
        password=os.getenv('REDIS_PASSWORD', None),
        socket_timeout=2,
        socket_connect_timeout=2,
        )

TWITTER_HANDLE = '@carolinespencer'
TWITTER_STATUS_ID = '748567826907136000'
DEFAULT_PHOTO = "https://d30y9cdsu7xlg0.cloudfront.net/png/370596-200.png"
PORT = 8040


tw_creds = os.getenv('TWITTER_API_CREDENTIALS').split(',')
TWITTER_AUTH = {}
TWITTER_AUTH['consumer_key'] = tw_creds[0]
TWITTER_AUTH['consumer_secret'] = tw_creds[1]
TWITTER_AUTH['access_token_key'] = tw_creds[2]
TWITTER_AUTH['access_token_secret'] = tw_creds[3]
