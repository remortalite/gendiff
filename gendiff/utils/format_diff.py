PREFIX_ADDED = "+"
PREFIX_REMOVED = "-"
PREFIX_NONE = " "


def get_item_name(name, *, prefix=PREFIX_NONE):
    return f"{prefix} {name}"


def sort_diff(data_dict):
    def _sort_func(key):
        sort_key_1 = 0 if key.startswith(PREFIX_REMOVED) else 1
        return key[len(PREFIX_REMOVED) + 1:], sort_key_1
    return dict(sorted(data_dict.items(),
                key=lambda x: _sort_func(x[0])))


def format_diff(data):
    result = {}

    for item in data:
        state_value = item["state"]

        match state_value:

            case "added":
                item_name = get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = item["value"]

            case "removed":
                item_name = get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"]

            case "notchanged":
                item_name = get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = item["value"]

            case "changed":
                item_name = get_item_name(item["name"], prefix=PREFIX_REMOVED)
                result[item_name] = item["value"][0]

                item_name = get_item_name(item["name"], prefix=PREFIX_ADDED)
                result[item_name] = item["value"][1]

            case "nested":
                item_name = get_item_name(item["name"], prefix=PREFIX_NONE)
                result[item_name] = format_diff(item["children"])

    return sort_diff(result)
