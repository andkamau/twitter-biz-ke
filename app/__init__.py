from flask import (Flask, g, request, session, redirect,
        url_for, render_template, jsonify)
from flask_script import Manager
import redis
import os
import config as config_file

app = Flask(__name__,
        template_folder=os.getenv('TW_TEMPLATES'),
        static_folder=os.getenv('TW_STATIC'))
app.config.from_object(config_file)

def get_db():
    if not hasattr(g, 'redis'):
        g.redis = redis.StrictRedis(**app.config['REDIS'])
    return g.redis

### VIEWS

@app.route('/data.json')
def get_data():
    '''
    '''
    try:
        db = get_db()
        resultset = {}
        for result in db.keys('*'):
            resultset[result] = db.get(result)

        return jsonify(resultset)

    except Exception, err:
        err = "ERROR: %s" % str(err)
        print err
        return '<html><body>%s</body></html>' % err

### END OF VIEWS

manager = Manager(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config_file.PORT, debug=True)
