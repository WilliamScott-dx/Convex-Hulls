"""
Gift-wrap Algorithm Tester
Author: William Scott
Date: 01/06/2015
Student Number: 11876177
"""


import sys
import math


def file_to_points():
    """Converts .dat file into list of points represented as tuples and returns the list"""
    points = []
    file = open(sys.argv[1])
    # First line not needed for how .dat file is read into array, read to get out of way
    file.readline()
    for line in file:
        line = line.strip('\n').split()
        line = (int(line[0]), int(line[1]))
        points.append(line)
    return points


def theta(point_a, point_b):
    """Computes an approximation of the angle between
    the line AB and a horizontal line through A."""
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]

    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6:
        return 360
    else:
        t = dy/(abs(dx) + abs(dy))

    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t += 4

    if t == 0:
        return 360

    return t*90


def gift_wrap(points):
    """Computes convex hull of a set of points, beginning with the lowest-rightmost point
    and selecting the next point that makes the minimum angle in a counter-clockwise direction."""
    i = 0
    v = 0
    k = find_min_point(points)
    n = len(points)
    hull = []
    points.append(points[k])

    while k != n:
        points[i], points[k] = points[k], points[i]
        hull.append(points[i])
        min_angle = 361
        for j in range(i + 1, n + 1):
            angle = theta(points[i], points[j])
            if v < angle < min_angle and points[i] != points[j]:
                min_angle = angle
                k = j
            # For collinear points
            elif angle == min_angle and points[i] != points[j]:
                compare_dist = distance(points[j], points[i])
                if compare_dist >= distance(points[k], points[i]):
                    k = j
        i += 1
        v = min_angle
    return hull


def distance(point_a, point_b):
    """Computes and returns the distance between two points"""
    a_to_b = math.hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])
    return a_to_b


def find_min_point(points):
    """Finds the lowest, rightmost point from a set of data, then returns its index"""
    smallest_point_index = 0
    for i in range(1, len(points)):
        if points[i][1] < points[smallest_point_index][1]:
            smallest_point_index = i
        elif points[i][0] > points[smallest_point_index][0] and points[i][1] == points[smallest_point_index][1]:
            smallest_point_index = i
    return smallest_point_index


def points_to_index(points, points_dict):
    """Returns a convex hull back as a list containing the points original index locations"""
    index_locations = ''
    for point in points:
        index_locations += str(points_dict[point]) + ' '
    return index_locations


def go():
    points = file_to_points()
    points_dict = {points[i]: i for i in range(len(points))}
    points = gift_wrap(points)
    index_locations = points_to_index(points, points_dict)
    print(index_locations)


if __name__ == '__main__':
    go()
