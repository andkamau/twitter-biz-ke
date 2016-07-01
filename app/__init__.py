from flask import (Flask, g, request, session, redirect,
        url_for, render_template)
from flask_script import Manager
import redis
import os
import api
import config as config_file

app = Flask(__name__,
        template_folder=os.getenv('TW_TEMPLATES'),
        static_folder=os.getenv('TW_STATIC'))
app.config.from_object(config_file)

def get_db():
    if not hasattr(g, 'redis'):
        g.redis = redis.StrictRedis(**app.config['REDIS'])
    return g.redis


class Twitter(object):

    def __init__(self):
        self.api = api.Api(**app.config['TWITTER_AUTH'])

    def fetch_all(self):
        pass


class Database(object):

    def __init__(self):
        self.db = get_db()

    def save(self, key, val):
        pass

    def fetch(self, key):
        return self.db.get('key') or None
