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
PORT = 8040


tw_creds = os.getenv('TWITTER_API_CREDENTIALS').split(',')
TWITTER_AUTH = {}
TWITTER_AUTH['consumer_key'] = tw_creds[0]
TWITTER_AUTH['consumer_secret'] = tw_creds[1]
TWITTER_AUTH['access_token_key'] = tw_creds[2]
TWITTER_AUTH['access_token_secret'] = tw_creds[3]

BLACKLIST = [
        '748806935047118848',
        '748607496932233216',
        '748622374111694849',
        '748590662988275713',
        '748797214508478464'
        ]
