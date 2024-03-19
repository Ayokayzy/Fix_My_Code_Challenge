#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=('GET', 'POST'), strict_slashes=False)
def status():
    """ Status of the web server
    """
    print("Hello")
    return jsonify({"status": "OK"})
