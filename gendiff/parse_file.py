import json
import yaml


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def parse_file(filename):
    data = None
    if filename.endswith("json"):
        with open(filename) as f:
            data = parse_json(f.read())
    elif filename.endswith("yml") or filename.endswith("yaml"):
        with open(filename) as f:
            data = parse_yaml(f.read())
    else:
        raise ValueError(f"Wrong exception at `{filename}`")
    return data
