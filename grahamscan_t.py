"""
Graham-scan Algorithm Tester
Author: William Scott
Date: 01/06/2015
Student Number: 11876177
"""

import sys
import operator
import math


def file_to_points():
    """Converts file into usable points"""
    points = []
    file = open(sys.argv[1])
    # First line not needed for how .dat file is read into array, read to get out of way
    file.readline()
    for line in file:
        line = line.strip('\n').split()
        line = (int(line[0]), int(line[1]))
        points.append(line)
    return points


def is_ccw(point_a, point_b, point_c):
    """Returns if a line is Counter-clockwise or not"""
    return is_on_line(point_a, point_b, point_c) > 0


def is_on_line(point_a, point_b, point_c):
    """Used to determine which side of the directed line made by point_a and point_b, that point_c lays.
    If it returns 0, the point is on the line
    If it returns >0 the point is counter-clockwise
    If it returns <0 the point is clockwise
    """
    return (point_b[0] - point_a[0]) * (point_c[1] - point_a[1]) - (point_b[1] - point_a[1]) * (point_c[0] - point_a[0])


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


def graham_scan(points):
    """Computes convex hull of a set of points, beginning with the lowest-rightmost point
    and selecting the next point if it makes a left turn when compared to the last two elements
    in the the working convex hull."""
    smallest_point_index = find_min_point(points)
    angle_list = create_angle_list(points, smallest_point_index)
    angle_list = [i[0] for i in angle_list]
    stack = [angle_list[0], angle_list[1], angle_list[2]]
    del angle_list[:3]
    while is_on_line(stack[0], stack[1], stack[2]) == 0:
        try:
            if distance(stack[0], stack[1]) > distance(stack[0], stack[2]):
                del stack[2]
            else:
                del stack[1]
            stack.append(angle_list[0])
            del angle_list[0]
        except IndexError:
            return stack

    for i in range(len(angle_list)):
        while not (is_ccw(stack[-2], stack[-1], angle_list[i])) and (len(stack) >= 3):
            stack.pop()
        stack.append(angle_list[i])

    #  Special case if last 2 points are collinear
    if is_on_line(stack[0], stack[-1], stack[-2]) == 0 and len(stack) > 3:
        del stack[-1]

    return stack


def distance(point_a, point_b):
    """Computes and returns the distance between two points"""
    a_to_b = math.hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])
    return a_to_b


def create_angle_list(points, smallest_point_index):
    """Returns a list containing tuples with the point and angle of that point when compared to
    the horizontal line through the point with the lowest point index."""
    angle_dict = {}
    for i in range(len(points)):
        angle_dict[points[i]] = theta(points[smallest_point_index], points[i])
    angle_dict[points[smallest_point_index]] = 0
    angle_list = sorted(angle_dict.items(), key=operator.itemgetter(1))
    return angle_list


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
    points = graham_scan(points)
    index_locations = points_to_index(points, points_dict)
    print(index_locations)

if __name__ == '__main__':
    go()
