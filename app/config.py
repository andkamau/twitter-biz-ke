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
        '748797214508478464',
        '748767834780512257',
        '748619671293804545',
        '749240812647682048',
        '749160405537320964',
        '748591144934735872',
        '748620437291143168',
        '748854402988007424',
        '748748227432751104',
        '748856275816054785',
        '748992711232000000',
        '748752649588137984',
        '748622096272605184',
        '748921541019205632',
        '748734657307373573',
        '748771250726588416',
        '749852277817606144',
        '748586743272710145',
        '748821836625051648',
        '748732523165790208',
        '748591537441763328',
        '748782397399797760',
        ]
