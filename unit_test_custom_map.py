from unittest import TestCase
from CustomMap import custom_map


class TestMapCustom(TestCase):
    def setUp(self) -> None:
        self.key_func = self.key_function
        self.value_func = self.value_function
        self.map_custom = custom_map

    # function for keys in dict
    @staticmethod
    def key_function(in_object: object) -> object:
        return in_object * 2

    # function for values in dict
    @staticmethod
    def value_function(in_object: object) -> object:
        return in_object * 2

    def test_map(self):
        result = self.map_custom(self.key_func, self.value_func, {"key1": 2, "key2": 4})
        self.assertEqual(next(result), ("key1key1", 4))
        self.assertEqual(next(result), ("key2key2", 8))

    def test_map_incorrect_type(self):
        with self.assertRaises(AttributeError):
            self.map_custom(self.key_func, self.value_func, ["key1", 2, "key2", 4])