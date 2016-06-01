from ...database import db, BaseMixin


class Post(db.Model, BaseMixin):
    __tablename__ = 'posts'

    title = db.Column(db.Unicode)
    text = db.Column(db.UnicodeText)
