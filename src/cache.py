cache = {}
repo_folder = {}

def set_repo_folder(folder):
    repo_folder['name'] = folder

def get_repo_folder():
    return repo_folder['name']

def add_to_cache(key, value):
    cache[key] = value

def get_from_cache(key):
    try: 
        return cache[key]
    except Exception:
        print e
        return {}

def invalidate_cache():
    cache = {}
