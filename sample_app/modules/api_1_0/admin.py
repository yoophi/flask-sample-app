from flask.ext.admin.contrib import sqla

from .models import Client, Token
from ...database import db
from ...extensions import admin

admin.add_view(sqla.ModelView(Client, db.session, 'Client'))
admin.add_view(sqla.ModelView(Token, db.session, 'Token'))
