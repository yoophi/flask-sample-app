from flask.ext.admin.contrib import sqla

from .models import Post
from ...database import db
from ...extensions import admin

admin.add_view(sqla.ModelView(Post, db.session, 'Post'))
