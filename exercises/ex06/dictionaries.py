"""Practice with dictionaries."""

__author__ = "730699395"


def invert(Input_string: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary"""
    Inversion: dict[str, str] = {}
    for key in Input_string:
        if Input_string[key] in Inversion:
            raise KeyError("You cannot have multiple of the same key")
        Inversion[Input_string[key]] = key
    return Inversion


def favorite_color(color: dict[str, str]) -> str:
    """Returns a string of the color that appears most frequently"""
    most_frequent: str = ""
    i: int = 0
    dictionary: dict[str, int] = {}
    for name in color:
        dictionary[color[name]] = 1
    for name in color:
        if color[name] in dictionary:
            dictionary[color[name]] += 1
            most_frequent = color[name]
    for name in dictionary:
        if dictionary[name] > i:
            i = dictionary[color[name]]
            most_frequent = name
    return most_frequent


def count(key_list: list[str]) -> dict[str, int]:
    """Counts the frequencies of keys in a list"""
    dictionary: dict[str, int] = {}
    for input_value in key_list:
        dictionary[input_value] = 0
    for input_value in dictionary:
        dictionary[input_value] += 1
    return dictionary
