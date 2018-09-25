#!flask/bin/python
from flask import Flask
from git_repository import clone_and_cache
from random import choice
from string import ascii_letters, digits
app = Flask(__name__)

def __build_temp_folder():
    random_string = ''.join([choice(ascii_letters + digits) for n in xrange(32)])
    return "/tmp/"+random_string

with app.app_context():
    temp_folder = __build_temp_folder()
    clone_and_cache(temp_folder)
    import routes
    app.run(debug=False, port=5050)
