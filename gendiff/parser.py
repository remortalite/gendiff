import json
import yaml
import os


def parse(data, format="json"):
    if format == "json":
        return json.loads(data)
    elif format in ("yml", "yaml"):
        return yaml.safe_load(data)
    raise ValueError("Wrong format! Needs: json/yaml file!")


def get_content(filename):

    ext = os.path.splitext(filename)[-1][1:]

    with open(filename) as f:
        data = parse(f.read(), ext)

    return data
