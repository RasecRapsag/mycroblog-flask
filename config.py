import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PUT_YOUR_SECRET_KEY_HERE'
    