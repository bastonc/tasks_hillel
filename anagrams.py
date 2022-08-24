# https://www.codeabbey.com/index/task_view/anagrams
# In many natural languages we can find some pairs of words which could be transformed to each other by changing the
# order of letters. I.e. they consist of the same set of letters, for example:
# cat - act take - teak ate - eat - tea
# Such words are called anagrams and as we see in the third example sometimes there are more than two words.
# Your task is to find out the amount of anagrams for given word by the dictionary.
# Input lines will contain a single word each.
# Answer should contain the number of anagrams for each word (not including the word itself).
# input data: bat, coal, lots
# answer: 1 1 2
from collections import Counter


def get_words_from_file() -> list:
    words = []
    with open("words.txt", "r") as f:
        for line in f:
            words.append(str(line).replace("\n", ""))
    return words


def search_anagram(word: str):
    count_anagrams = 0
    vocabulary = get_words_from_file()
    for word_from_vocabulary in vocabulary:
        if len(word) == len(word_from_vocabulary) and Counter(word) == Counter(word_from_vocabulary) and word != word_from_vocabulary:
            count_anagrams += 1
            # for check found words - uncomment line below
            # print(f"word: {word}, word in vocabulary: {word_from_vocabulary}")
    return count_anagrams


if __name__ == "__main__":
    assert(search_anagram("bat") == 1)
    assert(search_anagram("coal") == 1)
    assert(search_anagram("lots") == 2)
    print("Success")


