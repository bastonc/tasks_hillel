class custom_map:

    def __init__(self, func_key, func_val, iter_obj: dict):
        self.func_key = func_key
        self.func_val = func_val
        self.iter_obj = iter(iter_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        key_val = next(self.iter_obj)
        return self.func_key(key_val[0]), self.func_val(key_val[1])

