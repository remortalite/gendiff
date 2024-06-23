from gendiff.parser import get_content

import pytest


def test_parse_file():
    filepath_json = "tests/fixtures/file1_plain.json"
    expected = {"host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False}
    assert get_content(filepath_json) == expected

    filepath_yaml = "tests/fixtures/file1_plain.yaml"
    assert get_content(filepath_yaml) == expected

    with pytest.raises(ValueError):
        get_content("java.txt")
