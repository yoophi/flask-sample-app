from . import post_bp
from .models import Post

@post_bp.route('/', methods=['GET'])
def posts():
    return Post.query.first().title