# https://www.codeabbey.com/index/task_view/bit-count
# In this simple task you are to write a program which counts the number of non-zero bits in a given value.
# We are using 32-bit integer values, so there should be from 0 to 32 non-zero bits.


def bit_count(figure: int) -> int:
    binary_figure = "{:032b}".format(figure & 0xffffffff)
    count = 0
    for i in range(len(str(binary_figure))):
        if str(binary_figure[i]) == "1":
            count += 1
    return count


if __name__ == "__main__":
    assert (bit_count(100) == 3)
    assert (bit_count(1) == 1)
    assert (bit_count(-1) == 32)
    print("Success")
