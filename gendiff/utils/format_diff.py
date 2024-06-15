from gendiff.utils.formatters import format_diff_plain, format_diff_json


def format_diff(data, type="json"):
    if type == "json":
        return format_diff_json(data)
    elif type == "plain":
        return format_diff_plain(data)
