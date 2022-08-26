# https://www.codeabbey.com/index/task_view/linear-congruential-generator
# Here is the other method which is more widespread (it is implemented in most of programming languages and libraries)
# and still simple enough: let us start with some initial number and generate each new member Xnext of a sequence by the
# current Xcur using the following rule:
# Xnext = (A * Xcur + C) % M
# In this task we are going to build this algorithm to tell the value of n-th member of a sequence.
# Input data will contain the number of test-cases in the first line.
# Then test-cases will follow, each in separate line.
# Test-case consists of five values: A, C, M, X0, N where first three are the same as in formula, while X0 is the initial member of a sequence and N is the number of a member which we want to calculate.
# Answer should contain N-th member's value for each test-case, separated by spaces.

def linear_congruential(a, c, m, x0, n):
    x_cur = x0
    for _ in range(n):
        x_next = (a * x_cur + c) % m
        x_cur = x_next
    return x_next


if __name__ == "__main__":
    assert(linear_congruential(3, 7, 12, 1, 2) == 1)
    assert(linear_congruential(2, 3, 15, 8, 10) == 11)
    print("Success")

