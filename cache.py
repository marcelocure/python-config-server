cache = {}

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
