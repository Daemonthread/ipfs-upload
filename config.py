# -*- coding: utf-8 -*-

#Server Configuration
HOST = '0.0.0.0'
PORT = 9001
DEBUG = True
USE_RELOADER = True
SECRET_KEY = 'supersecretkey'

#DB Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DB_CREATED = False

# IPFS Configuration
IPFS_HOST = '127.0.0.1'
IPFS_PORT = 5001

# Redirect Configuration
SHORT_REDIRECT_DOMAIN = "http://{0}:{1}".format(HOST, PORT)
REDIRECT_BASE_URL = "http://ipfs.io/ipfs/"

# Upload Configuration
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
