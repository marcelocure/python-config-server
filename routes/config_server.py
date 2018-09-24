# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
from subprocess import call

from flask import current_app as app, request, jsonify
from cache import get_from_cache, get_repo_folder

def __pull(repo_folder):
    os.access(repo_folder, os.R_OK)
    call(["git", "pull"])

@app.route('/config', methods=['GET'])
def get_config():
    __pull(get_repo_folder())
    query = request.args.to_dict()
    service = query['service']
    return jsonify(get_from_cache(service))
