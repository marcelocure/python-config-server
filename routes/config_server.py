# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, request
from cache import get_from_cache

@app.route('/config', methods=['GET'])
def get_consultas(request):
    query = build_query(request.args.to_dict())
    service = query['service']
    return get_from_cache(service)
