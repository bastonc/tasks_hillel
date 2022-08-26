# https://www.codeabbey.com/index/task_view/funny-words-generator
# Let the words have arbitrary amount of letters, but letters at odd positions (1, 3, 5, ...) should be consonant,
# while letters ad even positions (2, 4, 6, ...) - like galaban, fanero - since such words are guaranteed to be easy to pronounce.
# Let agree that consonant letters are bcdfghjklmnprstvwxz and vowels are aeiou (note q and y are skipped).
# Implement simple Linear Congruential Generator with parameters
# A = 445, C = 700001, M = 2097152 - and initial value X0
# for sequence (i.e. seed) would be given to you as input data.
# To generate word consisting of N letters, generate the same amount of next random numbers with this generator,
# for example with X0 = 0 and N = 4 you'll get numbers 700001, 1821950, 1967079, 1537772.
# convert each of these random values to letter by taking modulo 19 for consonants or 5 for vowels and selecting the
# letter from the strings above (see step 2) simply by index.

import linear_congruential


def funny_words(*args):
    consonants = "bcdfghjklmnprstvwxz"
    vowels = "aeiou"
    final_words_list = []
    x0 = args[0]
    for count in args[1:]:
        final_word = ""
        index = 0
        while len(final_word) < count:
            digit = linear_congruential.linear_congruential(a=445, c=700001, m=2097152, x0=x0, n=1)
            x0 = digit
            if index % 2 == 0:
                final_word += consonants[digit % 19]
            else:
                final_word += vowels[digit % 5]
            index += 1
        final_words_list.append(final_word)
    return final_words_list


if __name__ == "__main__":
    assert(funny_words(0, 4, 5, 6) == ["fami", "wovaw", "kelasi"])
    assert (funny_words(2014, 9, 9, 9, 9) == ["foravanad", "zibecefeb", "wagabenip", "wedivonow"])
    print("Success")
