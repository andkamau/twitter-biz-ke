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
        resultset = []
        for result in db.keys('*'):
            resultset.append(eval(db.get(result)))
            if len(resultset) > 300:
                break

        print "*" * 40
        print resultset
        print "*" * 40
        return render_template('index.html', tweets=resultset)

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
    app.run(host='0.0.0.0', port=config_file.PORT, debug=True)
