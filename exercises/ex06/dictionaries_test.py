"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730699395"


def test_invert_edge() -> None:
    """One key and value edge test of the dictionary invert function"""
    input: dict[str, str] = {'a': 'b'}
    assert invert(input) == {'b': 'a'}


def test_invert_use_1() -> None:
    """Use test for invert with multiple keys and values"""
    input: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(input) == {'b': 'a', 'd': 'c', 'f': 'a'}


def test_invert_use_2() -> None:
    input: dict[str, str] = {'g': 'h', 'i': 'j', 'k': 'l'}
    assert invert(input) == {'h': 'g', 'j': 'i', 'l': 'k'}


def test_favorite_color_edge() -> None:
    """Edge test for favorite color with one name and color"""
    color: dict[str, str] = {"James": "Green"}
    assert favorite_color(color) == "Green"


def test_favorite_color_use_1() -> None:
    """Use test 1 for favorite color with multiple names and colors"""
    color: dict[str, str] = {"James": "Green", "Matthew": "Red"}
    assert favorite_color(color) == "Green"


def test_favorite_color_use_2() -> None:
    """Use test 2 for favorite color with multiple names and colors"""
    color: dict[str, str] = {"James": "Green", "Matthew": "Red", "Marsh": "Blue"}
    assert favorite_color(color) == "Green"


def test_count_edge() -> None:
    """Edge test for count with one value"""
    countx: list[str] = ['a']
    assert count(countx) == {'a': 1}


def test_count_use_1() -> None:
    """Use test 1 for count with multiple values"""
    countx: list[str] = ['a', 'b']
    assert count(countx) == {'a': 1, 'b': 1}


def test_count_use_2() -> None:
    """Use test 2 for count with multiple values"""
    countx: list[str] = ['a', 'a', 'b', 'b', 'b', 'c']
    assert count(countx) == {'a': 2, 'b': 3, 'c': 1}