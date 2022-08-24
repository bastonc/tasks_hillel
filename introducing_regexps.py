# https://www.codeabbey.com/index/task_view/introducing-regexps
# You are given a set of integers in decimal, octal, hex and binary format as they are used in several programming
# languages (derivatives from C and Assemblies):
# value consisting of digits 0-7 and starting with 0 is octal;
# value consisting of digits 0-9ABCDEF and starting with 0x is hexadecimal;
# hexadecimal could be instead suffixed by h but then it should not start with letter;
# binary could be written as 0b1000101 or 1000101b (though the single letter b is not a number);
# values consisting only of digits 0-9 are considered decimals (but not ones starting with zero - they should be regarded
# as octals and coul only contain digits 0-7).
# And your goal is to recognize these formats. Note that all letters (in hexadecimal values and in prefixes / suffixes)
# should be treated case-insensitively!

import re


def decode(string: str)-> str:
    if re.match("^0\d[0-7]", string):
        res = "oct"
    elif re.match("^0[x,X][0-9a-zA-Z]*", string) or re.match("^\d*h", string):
        res = "hex"
    elif re.match(".*[b,B].*", string):
        res = "bin"
    elif re.match("^[1-9]\d+", string) and not re.match(".*[a-zA-Z].*", string):
        res = "dec"
    else:
        res = "error"
    return res


if __name__ == "__main__":
    assert(decode("066") == "oct")
    assert(decode("068") == "error")
    assert (decode("068h") == "hex")
    assert(decode("0x80") == "hex")
    assert(decode("101b") == "bin")
    assert(decode("101") == "dec")
    print("Success")
