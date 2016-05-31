#!/usr/bin/env python
# coding: utf-8
from os import path

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore, Security

from .database import db
from .extensions import admin, config, cors, debug_toolbar, mail, oauth

__version__ = '0.1'

# Setup Flask-Security
from .core.models import Role, User

from .database import db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)

_current_dir = path.dirname(path.abspath(__file__))


def create_app(config_name):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    app = Flask(__name__,
                template_folder=(
                    path.join(_current_dir, '../templates')),
                static_folder=(
                    path.join(_current_dir, '../static')))

    config.init_app(app)
    app.config.from_yaml(config_name=config_name,
                         file_name='app.yml',
                         search_paths=[path.dirname(app.root_path)])
    app.config.from_heroku(keys=['SQLALCHEMY_DATABASE_URI', ])

    db.init_app(app)

    cors.init_app(app, resources={r"/v1/*": {"origins": "*"}})
    oauth.init_app(app)

    security.init_app(app)
    debug_toolbar.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    from .core import core as main_blueprint

    app.register_blueprint(main_blueprint)

    from .modules.posts import post_bp as post_blueprint

    app.register_blueprint(post_blueprint, url_prefix='/posts')

    from .modules.foo import mod as foo_blueprint

    app.register_blueprint(foo_blueprint, url_prefix='/foo')

    from .modules.api_1_0 import api as api_1_0_blueprint

    app.register_blueprint(api_1_0_blueprint, url_prefix='/v1')

    from .core.admin import admin as core_admin
    from .modules.api_1_0 import admin as api_admin
    from .modules.posts import admin as posts_admin
    from .modules.foo import admin as foo_admin

    return app


def create_app_min(config_name='default'):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    app = Flask(__name__)
    config.init_app(app)
    app.config.from_yaml(config_name=config_name,
                         file_name='app.yml',
                         search_paths=[path.dirname(app.root_path)])
    app.config.from_heroku(keys=['SQLALCHEMY_DATABASE_URI', ])

    return app

