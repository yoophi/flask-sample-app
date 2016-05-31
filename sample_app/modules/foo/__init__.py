from flask import Blueprint

mod = Blueprint('foo', __name__)

from . import views
