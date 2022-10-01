from CustomMap import CustomMap, map_custom


def key_func(in_object: object) -> object:
    return type(in_object)


def value_func(in_object: object) -> object:
    return type(in_object)


if __name__ == "__main__":
    # Simple dataset and solution by class
    print(CustomMap({True: 2, "two": 2}, key_func, value_func).custom_map())

    # Class in dataset and solution by function
    print(map_custom({CustomMap({1: 2}, None, None): 1}, key_func, value_func))
