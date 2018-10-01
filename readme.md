# Python Config Server
Config server written in python.

It has 2 endpoints available:
* GET /config/{service name}
* POST /config/refresh

## How does it work?
On startup, it clones a git repository informed on config.py and caches its data locally

On `GET /config/{service name}`, it gets the config for the given service name on the local cache

On `POST /config/refresh` it does a `git pull` and populates cache

## How to install?
`pip install -r requirements.txt`

## How to run?
`python src/api.py`