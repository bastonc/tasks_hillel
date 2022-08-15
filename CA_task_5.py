# https://www.codeabbey.com/index/task_view/prime-ranges
# Given several pairs of primes (like a, b) you are to tell for each of them the total quantity of primes in the range
# limited by these values (inclusive)
# Input data: will contain the amount of pairs in the first line.
# Next lines will contain one pair of primes each, the first value is always less than the second. All values will be less than 3000000.
# Answer should contain the quantity of primes in the ranges specified by these pairs.

def is_prime(figure: int):
    divider = 2
    while figure % divider != 0:
        divider += 1
    return divider == figure


def get_prime_in_range(start_int: int, stop_int: int):
    if start_int <= 3000000 and 3000000 >= stop_int > start_int:
        count = 0
        for figure in range(start_int, stop_int + 1):
            if is_prime(figure):
                count += 1
        return count
    else:
        print("Range error. Value must range < 3 000 000 and start int < stop int")


if __name__ == "__main__":
    assert(get_prime_in_range(5, 19) == 6)
    assert (get_prime_in_range(11, 29) == 6)
    assert (get_prime_in_range(2, 23) == 9)
    print("Success")

