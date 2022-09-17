def search_func(points: list) -> int:
    left_max = 0
    right_max = 0
    min_point = 0
    deep = 0
    for i in range(len(points)):
        if i > 0:
            if points[i] < points[i-1]:
                left_max = points[i-1]
                min_point = points[i]
            if points[i] < min_point:
                min_point = points[i]
            if points[i] > min_point:
                right_max = points[i]
                if right_max <= left_max:
                    new_deep = right_max - min_point
                else:
                    new_deep = left_max - min_point
                    left_max = right_max
                if new_deep > deep:
                    deep = new_deep
    return deep


if __name__ == "__main__":
    assert(search_func([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
    assert(search_func([9, 0, 9, 12, 2, 12]) == 10)
    print("Success")
