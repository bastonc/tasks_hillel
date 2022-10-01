class CustomMap:
    def __init__(self, in_dict: dict, func_key: object, func_value: object):
        self.in_dict = in_dict
        self.func_key = func_key
        self.func_value = func_value

    def custom_map(self):
        stop_iter = 0
        output_dict = {}
        key_val_tuple = iter(self.in_dict.items())
        while not stop_iter:
            try:
                key_val_all_tuple = next(key_val_tuple)
                output_dict.update({self.func_key(key_val_all_tuple[0]): self.func_value(key_val_all_tuple[1])})
            except StopIteration:
                stop_iter = 1
        return output_dict


def map_custom(in_dict: dict, func_key: object, func_value: object) -> dict:
    stop_iter = 0
    output_dict = {}
    key_val_tuple = iter(in_dict.items())
    while not stop_iter:
        try:
            key_val_all_tuple = next(key_val_tuple)
            output_dict.update({func_key(key_val_all_tuple[0]): func_value(key_val_all_tuple[1])})
        except StopIteration:
            stop_iter = 1
    return output_dict
