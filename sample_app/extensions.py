# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from flask.ext.config_helper import Config
from flask.ext.cors import CORS
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mail import Mail

admin = Admin()
config = Config()
cors = CORS()
debug_toolbar = DebugToolbarExtension()
mail = Mail()
