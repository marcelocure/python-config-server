# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, jsonify, request
from repositories.consulta import buscar, criar
import datetime

@app.route('/config', methods=['GET'])
def get_consultas():
    query = build_query(request.args.to_dict())
    service = query['service']
    
    return jsonify(buscar(query))
