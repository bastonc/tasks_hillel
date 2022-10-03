import datetime

from CustomMap import CustomMap, map_custom


def key_func(in_object: object) -> object:
    return in_object * 2


def value_func(in_object: object) -> object:
    return in_object * 2


if __name__ == "__main__":
    # Simple dataset and solution by class
    print(CustomMap({False: 2, "two": 2, "three": True}, key_func, value_func).custom_map())

    # Class in dataset and solution by function
    print(map_custom({CustomMap({1: 2}, None, None): 1}, key_func, value_func))
