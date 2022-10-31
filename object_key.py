
class Class_for_key():
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message


if __name__ == "__main__":
    test_dict = {}
    class1 = Class_for_key("I'am class1")
    class2 = Class_for_key("I'am class2")
    test_dict.update({class1: class1.get_message()})
    test_dict.update({class2: class2.get_message()})
    print(test_dict)
    print(test_dict[class1])
    print(test_dict[class2])

