#!flask/bin/python
from flask import Flask
from git import Repo
from random import choice
from string import ascii_letters, digits
from cache import add_to_cache, get_from_cache
from reader import read_dir
app = Flask(__name__)

def __cache_configs(temp_folder):
    services = read_dir(temp_folder)
    for service in services:
        add_to_cache(service.keys()[0], service.values()[0])

def __build_temp_folder():
    random_string = ''.join([choice(ascii_letters + digits) for n in xrange(32)])
    return "/tmp/"+random_string

with app.app_context():
    temp_folder = __build_temp_folder()
    Repo.clone_from("https://github.com/marcelocure/config.git", temp_folder)
    __cache_configs(temp_folder)
    import routes
    app.run(debug=True)
