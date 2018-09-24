# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, request, jsonify
from cache import get_from_cache

@app.route('/config', methods=['GET'])
def get_config():
    query = request.args.to_dict()
    service = query['service']
    return jsonify(get_from_cache(service))
