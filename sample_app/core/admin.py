from flask.ext.admin.contrib import sqla

from .models import User
from ..database import db
from ..extensions import admin

admin.add_view(sqla.ModelView(User, db.session, 'User'))
