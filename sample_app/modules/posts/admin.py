from flask.ext.admin.contrib import sqla

from sample_app.database import db
from sample_app.extensions import admin
from .models import Post

admin.add_view(sqla.ModelView(Post, db.session, 'Post'))
