

def map_custom(in_dict: dict, func_key: object, func_value: object) -> dict:
    output_dict = {}
    for key_val_tuple in in_dict.items():
        output_dict.update({func_key(key_val_tuple[0]): func_value(key_val_tuple[1])})
    return output_dict
