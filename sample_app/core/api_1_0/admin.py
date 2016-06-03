from flask.ext.admin.contrib import sqla

from sample_app.database import db
from sample_app.extensions import admin
from .models import Client, Token

admin.add_view(sqla.ModelView(Client, db.session, 'Client'))
admin.add_view(sqla.ModelView(Token, db.session, 'Token'))
