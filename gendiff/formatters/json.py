from . import stylish

import json


def format(data):
    return json.dumps({"root": data})
