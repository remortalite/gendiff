from gendiff.make_diff import make_diff
from gendiff.parse import parse_by_filename
from gendiff.formatters import stylish_formatter

import json
import pytest


@pytest.fixture
def make_test_data_1():
    with open("tests/fixtures/file1_plain.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_test_data_2():
    with open("tests/fixtures/file2_plain.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_test_result():
    with open("tests/fixtures/file1_2_diff.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def make_format_diff_str():
    with open("tests/fixtures/file1_2_result.json") as f:
        result = json.load(f)
    return result


@pytest.fixture
def nested_data_1():
    result = parse_by_filename("tests/fixtures/file1_nested.yaml")
    return result


@pytest.fixture
def nested_data_2():
    result = parse_by_filename("tests/fixtures/file2_nested.yaml")
    return result


@pytest.fixture
def nested_data_expected_dict():
    result = parse_by_filename("tests/fixtures/file1_2_nested_diff.json")
    return result


@pytest.fixture
def nested_data_expected_diff():
    result = parse_by_filename("tests/fixtures/file1_2_nested_result.json")
    return result

