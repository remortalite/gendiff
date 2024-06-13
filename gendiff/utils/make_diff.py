from gendiff.utils.format_diff import format_diff, sort_diff


def _prepare_data_item(name, state, value, is_nested=False):
    return {"name": name,
            "state": state,
            "children" if is_nested else "value": value}


def make_diff(data1, data2):

    result_data = []

    common_keys = set(data1) & set(data2)
    added_keys = set(data2) - set(data1)

    all_keys = set(data1) | set(data2)

    nested_keys = set()
    # check if nested
    for key in all_keys:
        if all(isinstance(x.get(key), dict) for x in (data1, data2)):
            nested_keys.add(key)

    for key in all_keys - nested_keys:
        if key in set(data1) ^ set(data2):
            status = value = None
            if key in added_keys:
                status = "added"
                value = data2[key]
            else:
                status = "removed"
                value = data1[key]
            new_data = _prepare_data_item(key, status, value)

        else:
            if data1[key] == data2[key]:
                new_data = _prepare_data_item(key, "notchanged", data1[key])
            else:
                new_data = _prepare_data_item(key, "changed", [data1[key], data2[key]])

        result_data.append(new_data)

    for key in nested_keys:
        new_data = make_diff(data1[key], data2[key])
        result_data.append(_prepare_data_item(key, "nested", new_data, is_nested=True))

    return result_data


def make_and_format_diff(data1, data2):
    return sort_diff(format_diff(make_diff(data1, data2)))
