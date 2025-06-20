import json

def get_db_config(fname):
    with open(fname, 'r') as f:
        # with open('./data/config.json', 'r') as f:
        config = json.load(f)
    return config
