from reader import read_dir
import os
from subprocess import call
from cache import add_to_cache, set_repo_folder
from config import repository

def clone_and_cache(temp_folder):
    set_repo_folder(temp_folder)
    call(["git", "clone", repository, temp_folder])
    __cache_configs(temp_folder)

def __cache_configs(temp_folder):
    services = read_dir(temp_folder)
    for service in services:
        add_to_cache(service.keys()[0], service.values()[0])

def pull(repo_folder):
    os.chdir(repo_folder)
    call(["git", "pull"])
    __cache_configs(repo_folder)
