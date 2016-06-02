#!/usr/bin/env python
# coding: utf-8
from os import path

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore, Security

from sample_app.database import db
from sample_app.extensions import admin, config, cors, debug_toolbar, mail, oauth

__version__ = '0.1'

# Setup Flask-Security
from sample_app.core.models import Role, User  # NOQA
from sample_app.database import db  # NOQA

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)

_current_dir = path.dirname(path.abspath(__file__))


def create_app(config_name='default'):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    app = create_app_min(config_name)

    cors.init_app(app, resources={r"/v1/*": {"origins": "*"}})
    oauth.init_app(app)
    security.init_app(app)
    debug_toolbar.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

    from sample_app.core import core as main_blueprint

    app.register_blueprint(main_blueprint)

    from sample_app.modules.posts import post_bp as post_blueprint

    app.register_blueprint(post_blueprint, url_prefix='/posts')

    from sample_app.modules.thingy import mod as foo_blueprint

    app.register_blueprint(foo_blueprint, url_prefix='/thingy')

    from sample_app.core.api_1_0 import api as api_1_0_blueprint

    app.register_blueprint(api_1_0_blueprint, url_prefix='/v1')

    import sample_app.core.admin
    import sample_app.modules.posts.admin
    import sample_app.modules.thingy.admin

    return app


def create_app_min(config_name='default'):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    template_folder = path.join(_current_dir, '../templates')
    static_folder = path.join(_current_dir, '../static_folder')
    app = Flask(__name__,
                template_folder=template_folder,
                static_folder=static_folder)
    config.init_app(app)
    app.config.from_yaml(config_name=config_name,
                         file_name='app.yml',
                         search_paths=[path.dirname(app.root_path)])
    app.config['PROJECT_ROOT'] = app.root_path

    db.init_app(app)

    return app
