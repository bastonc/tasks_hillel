# https://www.codeabbey.com/index/task_view/palindromes
# The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
# As you see, case of the letters is ignored. Spaces and punctuations are ignored too.
# Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
# Input data contains number of phrases in the first line.
# Next lines contain one phrase each.
# Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.

import re


def check_palindrome(string: str) -> str:
        clean_string = ''
        for char in string.lower():
            if re.match("[a-z]", char):
                clean_string += char
        if clean_string == clean_string[::-1]:
            return "Y"
        return "N"


if __name__ == "__main__":
    assert (check_palindrome("Stars") == "N")
    assert (check_palindrome("O, a kak Uwakov lil vo kawu kakao!") == "Y")
    assert (check_palindrome("Some men interpret nine memos") == "Y")
    print("Success")
