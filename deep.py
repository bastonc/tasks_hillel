def search_deep(points: list) -> int:
    left_max = 0
    min_point = 0
    deep = 0
    for i in range(len(points)):
        if i > 0:
            if points[i] < points[i-1]:
                if points[i-1] > left_max:
                    left_max = points[i-1]
                min_point = points[i]
            elif points[i] < min_point:
                min_point = points[i]
            elif points[i] > min_point:
                right_max = points[i]
                new_deep = min(left_max, right_max) - min_point
                if new_deep > deep:
                    deep = new_deep
    return deep


if __name__ == "__main__":
    assert(search_deep([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
    assert(search_deep([9, 0, 9, 12, 2, 12]) == 10)
    assert (search_deep([1, 1, 9, 12, 18, 12]) == 0)
    assert (search_deep([1, 1, 9, 12, 9, 12]) == 3)
    assert (search_deep([1, 1]) == 0)
    print("Success")
