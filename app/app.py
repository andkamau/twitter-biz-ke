import redis, os, tweepy, config
from flask import render_template

def get_twitter_api_credentials():
    creds = os.getenv('TWITTER_API_CREDENTIALS').split(',')
    auth = tweepy.OAuthHandler(creds[0], creds[1])
    auth.set_access_token(creds[2], creds[3])
    return tweepy.API(auth)


class Twitter(object):

    def __init__(self):
        self.api = get_twitter_api_credentials()
        self.db = redis.StrictRedis(**config.REDIS)

    def fetch_all(self, maxid=None):
        result = self.api.search(q=config.TWITTER_HANDLE, result_type='recent', count=100, max_id=maxid)
        # result is a tweepy.models.SearchResults
        false_count = true_count = 0
        ids = []
        for each in result:
            ids.append(each.id)
            resultset = {}
            # each is a tweepy.models.Status
            if not each.in_reply_to_status_id_str == config.TWITTER_STATUS_ID:
                false_count += 1
                continue
            else:
                true_count += 1
                resultset['date'] = str(each.created_at)
                resultset['id'] = each.id_str
                resultset['name'] = each.user.screen_name
                resultset['description'] = each.text.replace(config.TWITTER_HANDLE, '')
                resultset['retweets'] = each.retweet_count
                resultset['faves'] = each.favorite_count
                try:
                    resultset['link'] = each.entities['urls'][0]['display_url']
                except:
                    resultset['link'] = ""
                try:
                    resultset['photo'] = each.entities['media'][0]['media_url']
                except:
                    resultset['photo'] = each.user.profile_image_url.replace('_normal', '')

                self.db.set(str(each.id), resultset)

        ids.sort()
        max_id = ids[len(ids)-1]
        min_id = ids[0]
        print "%d tweets added" % true_count
        print "%d tweets were not direct replies" % false_count
        print "Max ID: %s | Min ID: %s" % (str(max_id), str(min_id))

        return max_id, min_id
