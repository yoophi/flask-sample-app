from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

from . import api, users


@api.route('/sample')
def do_sample():
    return jsonify({'result': 'sample'})
