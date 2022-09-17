# https://www.codeabbey.com/index/task_view/triangle-area
# Being able to calculate area of triangle is quite important since many more complex tasks are often easily reduced to
# this (and we will use it too later).
# One of the oldest known methods is Heron's Formula which takes as inputs the lengths of the triangle's sides.
#
# In this problem you however is to write a program which uses X and Y coordinates of the triangle's vertices instead.
# 'So you can use either this formula somehow or find another one.
# Input data will contain the number of triangles to process.
# Next lines will contain 6 values each, in order X1 Y1 X2 Y2 X3 Y3, describing three vertices of a triangle.

from math import sqrt


def area_triangle(x1, y1, x2, y2, x3, y3):
    # Calculate edges
    a = sqrt((x2 - x1)**2 + (y2-y1)**2)
    b = sqrt((x3 - x1)**2 + (y3-y1)**2)
    c = sqrt((x3 - x2)**2 + (y3-y2)**2)
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    # Area by Heron's Formula https://en.wikipedia.org/wiki/Heron%27s_formula
    area = sqrt(s*((s-a)*(s-b)*(s-c)))
    return round(area) if round(area, 1) % 1 == 0 else round(area, 2)


if __name__ == "__main__":
    assert(area_triangle(1, 3, 9, 5, 6, 0) == 17)
    assert (area_triangle(1, 0, 0, 1, 10000, 10000) == 9999.5)
    assert (area_triangle(7886, 5954, 9953, 2425, 6250, 2108) == 6861563)
    print("Success")

