# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from flask.ext.config_helper import Config
from flask.ext.cors import CORS
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mail import Mail
from flask.ext.oauthlib.provider import OAuth2Provider
from flask_bootstrap import Bootstrap
from flask_thumbnails_s3 import Thumbnail

admin = Admin()
config = Config()
cors = CORS()
debug_toolbar = DebugToolbarExtension()
mail = Mail()
oauth = OAuth2Provider()
bootstrap = Bootstrap()
thumbnail = Thumbnail()
