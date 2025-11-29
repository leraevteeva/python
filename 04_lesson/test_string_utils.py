import pytest
from string_utils import StringUtils

utils = StringUtils()


# capitalize

def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_space():
    assert utils.capitalize(" ") == " "


def test_capitalize_none():
    with pytest.raises(TypeError):
        utils.capitalize(None)


# trim

def test_trim_positive():
    assert utils.trim("   skypro   ") == "skypro"


def test_trim_empty():
    assert utils.trim("") == ""


def test_trim_only_spaces():
    assert utils.trim("     ") == ""


def test_trim_none():
    with pytest.raises(TypeError):
        utils.trim(None)


# to_list

def test_to_list_default_delimiter():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]


def test_to_list_custom_delimiter():
    assert utils.to_list("a:b:c", ":") == ["a", "b", "c"]


def test_to_list_empty_string():
    assert utils.to_list("") == []


def test_to_list_none():
    with pytest.raises(TypeError):
        utils.to_list(None)


# contains

def test_contains_positive():
    assert utils.contains("skypro", "pro") is True


def test_contains_negative():
    assert utils.contains("skypro", "xyz") is False


def test_contains_empty_substring():
    assert utils.contains("abc", "") is True


def test_contains_none_string():
    with pytest.raises(TypeError):
        utils.contains(None, "x")


def test_contains_none_substring():
    with pytest.raises(TypeError):
        utils.contains("abc", None)
