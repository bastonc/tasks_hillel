# https://www.codeabbey.com/index/task_view/arithmetic-progression
# When we speak about arithmetic progression (or arithmetic sequence) we mean a series of numbers with a special  \
#         property - each value is followed by the other, greater by predefined amount (step).
# I.e. difference of (K+1)-th and K-th values is a constant. Here are examples of sequences
# Since so, arithmetic sequence is completely defined by the first member (A) and the increment value - step size - (B).
#     First few members could be expressed as A + (A + B) + (A + 2B) + (A + 3B) + ...
# You are to calculate the sum of first members of arithmetic sequence. Wikipedia page on arithmetic progression could
# be of significant help to one who meets them for the first time.


def progression(a, b, n):
    return n * (2 * a + (n - 1) * b) // 2


if __name__ == "__main__":
    assert(progression(5, 2, 3) == 21)
    assert (progression(3, 0, 10) == 30)
    print("Success")
