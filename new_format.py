def new_format(figure: str):
    figure_str = str(figure)[::-1]
    return '.'.join(figure_str[i:i + 3] for i in range(0, len(figure_str), 3))[::-1]


if __name__ == '__main__':
    assert (new_format("1000000") == "1.000.000")
    assert (new_format("100") == "100")
    assert (new_format("1000") == "1.000")
    assert (new_format("100000") == "100.000")
    assert (new_format("10000") == "10.000")
    assert (new_format("0") == "0")
    print("Successful")
