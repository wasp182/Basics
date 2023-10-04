def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


animals={
    "lion": "scary",
    "elephant":"big",
    "teddy":"soft",
}

test = my_deepcopy(animals)
print(test)
test["lion"]="testing"
print(test["lion"])
print(animals["lion"])