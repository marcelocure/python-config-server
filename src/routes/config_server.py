# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, request, jsonify
from cache import get_from_cache, get_repo_folder
from git_repository import pull

@app.route('/config/<service>', methods=['GET'])
def get_config(service):
    return jsonify(get_from_cache(service)), 200

@app.route('/config/refresh', methods=['POST'])
def refresh_config():
    try:
        pull(get_repo_folder())
        return jsonify({}), 200
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500
