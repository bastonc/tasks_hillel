# https://www.codeabbey.com/index/task_view/matching-brackets
# We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones.
# The goal is to check, whether brackets are in correct sequence. I.e. any opening bracket should have closing bracket of
# the same type somewhere further by the string, and bracket pairs should not overlap, though they could be nested:
# Input data will contain number of testcases in the first line.
# Then specified number of lines will follow each containing a test-case in form of a character sequence.
# Answer should contain 1 (if bracket order is correct) or 0 (if incorrect) for each of test-cases, separated by spaces.

class Buckets:
    def __init__(self, buckets_list: list = [["(", ")"], ["{", "}"], ["[", "]"], ["<", ">"]]):
        self.bucket_open = list()
        self.buckets = buckets_list

    def open_add(self, char: str) -> None:
        self.bucket_open.append(char)

    def is_empty(self) -> bool:
        if not self.bucket_open:
            return True
        return False

    def compare(self, char: str) -> bool:
        open_bucket = self.bucket_open.pop()
        for index, bucket in enumerate(self.buckets):
            if char == bucket[1] and open_bucket == self.buckets[index][0]:
                return True
        return False


def brackets_balance(string: str):
    flag = 1
    buckets = Buckets()
    for char in string:
        if char in "({[<":
            buckets.open_add(char)
        elif char in ")}]>":
            if buckets.is_empty():
                flag = 0
                break
            if buckets.compare(char):
                continue
            flag = 0
            break
    if not buckets.is_empty():
        flag = 0
    return flag


if __name__ == "__main__":
    assert (brackets_balance("(a+[b*c]-{d/3})") == 1)
    assert (brackets_balance("(a + [b * c) - 17]") == 0)
    assert (brackets_balance("(((a * x) + [b] * y) + c") == 0)
    assert (brackets_balance("auf(zlo)men [gy<psy>] four{s}") == 1)
    print("Success")
