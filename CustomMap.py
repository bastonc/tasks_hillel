class CustomMap:
    def __init__(self, in_dict: dict, func_key: object, func_value: object):
        self.in_dict = in_dict
        self.func_key = func_key
        self.func_value = func_value

    def custom_map(self):
        output_dict = {}
        for key_val_tuple in self.in_dict.items():
            output_dict.update({self.func_key(key_val_tuple[0]): self.func_value(key_val_tuple[1])})
        return output_dict


def map_custom(in_dict: dict, func_key: object, func_value: object) -> dict:
    output_dict = {}
    for key_val_tuple in in_dict.items():
        output_dict.update({func_key(key_val_tuple[0]): func_value(key_val_tuple[1])})
    return output_dict
