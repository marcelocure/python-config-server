import os
# from flask import jsonify
import json
from functools import reduce

def __get_file_content(file_path):
    with open(file_path) as f:
        return reduce(lambda p, n: p+n, f.readlines())

def __remove_extension(file_name):
    return file_name[:file_name.index('.')]

def __read_file(file_name, path):
    file_path = '{0}/{1}'.format(path, file_name)
    if not os.path.isdir(file_path):
        return { __remove_extension(file_name): json.loads(__get_file_content(file_path)) }

def read_dir(path):
    dirlist = os.listdir(path)
    return filter(lambda v: v is not None, map(lambda filename: __read_file(filename, path), dirlist))
