
from CustomMap import map_custom


# function for keys in dict
def key_func(in_object: object) -> object:
    return in_object * 2


# function for values in dict
def value_func(in_object: object) -> object:
    return in_object * 2


if __name__ == "__main__":
    assert(map_custom({"key1": 2, "key2": 4}, key_func, value_func) == {"key1key1": 4, "key2key2": 8})
    print("Success")
