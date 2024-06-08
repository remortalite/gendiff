from gendiff.utils.make_diff import *
from gendiff.utils.parse_file import parse_file

import json
import pytest



@pytest.fixture
def make_test_data_1():
	with open("tests/fixtures/make_diff_data_1.json") as f:
		result = json.load(f)
	return result


@pytest.fixture
def make_test_data_2():
	with open("tests/fixtures/make_diff_data_2.json") as f:
		result = json.load(f)
	return result


@pytest.fixture
def make_test_result():
	with open("tests/fixtures/make_diff_result.json") as f:
		result = json.load(f)
	return result


@pytest.fixture
def make_format_diff_str():
	with open("tests/fixtures/make_format_diff_result.json") as f:
		result = json.load(f)
	return result


@pytest.fixture
def nested_data_1():
	result = parse_file("tests/fixtures/make_diff_nested_1.yaml")
	return result


@pytest.fixture
def nested_data_2():
	result = parse_file("tests/fixtures/make_diff_nested_2.yaml")
	return result


@pytest.fixture
def nested_data_expected_dict():
	result = parse_file("tests/fixtures/nested_data_expected_dict.json")
	return result


@pytest.fixture
def nested_data_expected_diff():
	result = parse_file("tests/fixtures/nested_data_expected_diff.json")
	return result


def _sort_by_name(data):
		return sorted(data, key=lambda x: x['name'])


def test_make_diff(make_test_data_1, make_test_data_2, make_test_result):
	result = make_diff(make_test_data_1, make_test_data_2)
	result = _sort_by_name(result)
	make_test_result = _sort_by_name(make_test_result)
	assert result == make_test_result
	assert make_diff({}, {}) == []


def test_make_diff_nested(nested_data_1, nested_data_2, nested_data_expected_diff):
	result = make_diff(nested_data_1, nested_data_2)
	expected = nested_data_expected_diff
	result = _sort_by_name(result)
	expected = _sort_by_name(expected)
	assert result == expected


def test_make_and_format_diff_nested(nested_data_1, nested_data_2, nested_data_expected_dict):
	result = make_and_format_diff(nested_data_1, nested_data_2)
	expected = nested_data_expected_dict
	assert result == expected


def test_make_and_format_diff(make_test_data_1, make_test_data_2, make_format_diff_str):
	result = make_and_format_diff(make_test_data_1, make_test_data_2)
	assert result == make_format_diff_str
	assert make_and_format_diff({}, {}) == {}
