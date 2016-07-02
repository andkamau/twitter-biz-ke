from flask import (Flask, g, request, session, redirect,
        url_for, render_template, jsonify)
from flask_script import Manager
import redis, os, datetime
import config as config_file


app = Flask(__name__)
app.config.from_object(config_file)


def get_db():
    if not hasattr(g, 'redis'):
        g.redis = redis.StrictRedis(**app.config['REDIS'])
    return g.redis

### VIEWS

@app.route('/')
def get_data():
    '''
    '''
    try:
        db = get_db()
        top_resultset = mid1_resultset = mid2_resultset = low_resultset = []
        for result in db.keys('*'):
            resp = eval(db.get(result))
            try:
                if int(resp['retweets']) + int(resp['faves']) > 50:
                    top_resultset.append(resp)
                    print resp['retweets']
                elif int(resp['retweets']) + int(resp['faves']) > 25:
                    mid1_resultset.append(resp)
                elif int(resp['retweets']) + int(resp['faves']) > 10:
                    mid2_resultset.append(resp)
                elif int(resp['retweets']) + int(resp['faves']) == 0:
                    low_resultset.append(resp)
                else:
                    mid2_resultset.append(resp)
            except:
                low_resultset.append(resp)

        return render_template('index.html',
                top_tweets=top_resultset,
                mid1_tweets=mid1_resultset,
                mid2_tweets=mid2_resultset,
                low_tweets=low_resultset)

    except Exception, err:
        err = "ERROR: %s" % str(err)
        print err
        return '<html><body>%s</body></html>' % err
        

@app.route("/test")
def main():
    return render_template('index.html')

### END OF VIEWS

manager = Manager(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config_file.PORT)
