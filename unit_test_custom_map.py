from unittest import TestCase
from CustomMap import map_custom


class TestMapCustom(TestCase):
    def setUp(self) -> None:
        self.key_func = self.key_function
        self.value_func = self.value_function
        self.map_custom = map_custom

    # function for keys in dict
    @staticmethod
    def key_function(in_object: object) -> object:
        return in_object * 2

    # function for values in dict
    @staticmethod
    def value_function(in_object: object) -> object:
        return in_object * 2

    def test_map(self):
        self.assertEqual(self.map_custom({"key1": 2, "key2": 4}, self.key_func, self.value_func), {"key1key1": 4,
                                                                                                   "key2key2": 8})

    def test_map_incorrect_type(self):
        with self.assertRaises(AttributeError):
            self.map_custom(["key1", 2, "key2", 4], self.key_func, self.value_func)
