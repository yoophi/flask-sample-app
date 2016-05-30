from flask.ext.admin.contrib import sqla

from ..database import db
from .models import User
from ..extensions import admin

admin.add_view(sqla.ModelView(User, db.session, 'User'))
