#  This is a mission to check the similarity of two triangles.
#
# You are given two lists as coordinates of vertices of each triangle.
# You have to return a bool. (The triangles are similar or not)
#
# Example:
# similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
# similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
# similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
#  Input:
#  Two lists as coordinates of vertices of each triangle.
#  Coordinates is three tuples of two integers.
#
#  Output: True or False.
#
#  Precondition:
#  -10 ≤ x(, y) coordinate ≤ 10

from typing import List, Tuple
from math import sqrt
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    ab_0 = sqrt((coords_1[1][0] - coords_1[0][0]) ** 2 + (coords_1[1][1] - coords_1[0][1]) ** 2)
    bc_0 = sqrt((coords_1[2][0] - coords_1[1][0]) ** 2 + (coords_1[2][1] - coords_1[1][1]) ** 2)
    ca_0 = sqrt((coords_1[0][0] - coords_1[2][0]) ** 2 + (coords_1[0][1] - coords_1[2][1]) ** 2)

    ab_1 = sqrt((coords_2[1][0] - coords_2[0][0]) ** 2 + (coords_2[1][1] - coords_2[0][1]) ** 2)
    bc_1 = sqrt((coords_2[2][0] - coords_2[1][0]) ** 2 + (coords_2[2][1] - coords_2[1][1]) ** 2)
    ca_1 = sqrt((coords_2[0][0] - coords_2[2][0]) ** 2 + (coords_2[0][1] - coords_2[2][1]) ** 2)

    triangle_0 = sorted([ab_0, bc_0, ca_0])
    triangle_1 = sorted([ab_1, bc_1, ca_1])

    if triangle_0[0]/triangle_1[0] == triangle_0[1]/triangle_1[1] == triangle_0[2]/triangle_1[2]:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")


