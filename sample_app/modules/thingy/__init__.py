from flask import Blueprint

mod = Blueprint('thingy_bp', __name__)

from . import views
