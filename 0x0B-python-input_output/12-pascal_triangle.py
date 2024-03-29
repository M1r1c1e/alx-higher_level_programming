#!/usr/bin/python3
"""Defineing a Pascal's Triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returning a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_ang= triangles[-1]
        tmp = [1]
        for i in range(len(tri_ang) - 1):
            tmp.append(tri_ang[i] + tri_ang[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
