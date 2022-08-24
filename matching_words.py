# https://www.codeabbey.com/index/task_view/matching-words
# Ali-Baba found a secret cave with treasures, stored by The Forty Thieves. However, famous magical phrase Open Sesame
# obviously does not work.
# # Instead there is a long and strange text inscribed on the stone wall - and Ali-Baba guessed that one should find
# matching words in this inscription (i.e. ones which are encountered more than once) and pronounce them in alphabetical
# order.
# # We are to help the poor craftsman to access the thieves' treasury. Let's write a program that sieves necessary words
# from the given text, and prints them in the proper order.
# # Input data consist of about 300 words, each made of 3 Latin letters. The end is signaled by the word end.
# Answer should contain all the words which are encountered more than once in lexicographic order.
from collections import Counter


def search_key(string: str):
    keys = []
    key_list = string.split()
    counter_key = Counter(key_list)
    for key in counter_key.keys():
        if counter_key[key] > 1:
            keys.append(key)
    return sorted(keys)


if __name__ == "__main__":
    assert(search_key("nun lam mip tex bal pif sot bal bod tex end") == ["bal", "tex"])
    print("Success")
