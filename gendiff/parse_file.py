import json
import yaml


def parse(data, format):
    match format:
        case "json":
            return json.loads(data)
        case "yaml":
            return yaml.safe_load(data)
        case _:
            raise ValueError("Wrong format!")


def parse_file(filename):
    data = None
    if filename.endswith("json"):
        with open(filename) as f:
            data = parse(f.read(), "json")
    elif filename.endswith("yml") or filename.endswith("yaml"):
        with open(filename) as f:
            data = parse(f.read(), "yaml")
    else:
        raise ValueError(f"Wrong exception at `{filename}`")
    return data
