# https://www.codeabbey.com/index/task_view/two-printers
# John and Mary founded J&M publishing house and bought two old printers to equip it.
# Now they have their first commercial deal - to print a document consisting of N pages.
# It appears that printers work at different speed. One produces a page in X seconds and other does it in Y seconds.
# So now company founders are curious about minimum time they can spend on printing the whole document with two
# printers.
# N will not exceed 1,000,000,000.


def two_printers(x, y, n):
    if n < 1000000000:
        first_printer = int(y * n / (x + y))
        second_printer = int(x * n / (x + y))
        first_time = int(max((first_printer + 1) * x, second_printer * y))
        second_time = int(max(first_printer * x, (second_printer + 1) * y))
        return min(first_time, second_time)
    return "Incorrect N"


if __name__ == "__main__":
    assert(two_printers(1, 1, 5) == 3)
    assert(two_printers(3, 5, 4) == 9)
    print("Success")
