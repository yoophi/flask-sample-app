from flask import render_template

from . import core


@core.route('/', methods=['GET'])
def index():
    return render_template('index.html')

