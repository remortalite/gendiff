from gendiff.formatters import (json_formatter,
                                plain_formatter,
                                stylish_formatter)


def format_data(data, output_type="json", formatter=None):
    if not formatter:
        match output_type:
            case "json":
                formatter = json_formatter
            case "plain":
                formatter = plain_formatter
            case _:
                formatter = stylish_formatter
    return formatter(data)
