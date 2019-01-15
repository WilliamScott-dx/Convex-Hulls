"""
Gift-wrap Algorithm Evaluator
Author: William Scott
Date: 01/06/2015
Student Number: 11876177
"""


import random
import time
from giftwrap_t import *


def generate_points(size=1000, shape="square"):
    """Randomly generates points in the shape of a circle or square"""
    if shape is "square":
        points = []
        for i in range(size):
            points.append((random.randint(0, 1000), random.randint(0, 1000)))
            i += 1
        return points

    if shape == "circle":
        points = []
        i = 0
        while i < size:
            point = (random.randint(0, 1000), random.randint(0, 1000))
            if (((point[0] - 500) ** 2) + ((point[1] - 500) ** 2)) < 250000:
                points.append(point)
                i += 1
        return points


def tester(size=1000, shape="square"):
    times = []
    average_time = 0

    for i in range(5):
        points = generate_points(size, shape)
        start = time.time()
        gift_wrap(points)
        end = time.time()
        time_taken = end - start
        times.append(time_taken)

    for recorded_time in times:
        average_time += recorded_time
    average_time /= 5

    test_result = "Giftwrap {0!s} with {1!s} points: Averaged {2!s}s over 5 trials.".format(shape, size, average_time)
    print(test_result)


def go():
    # Test Square
    tester(1000, "square")
    tester(2000, "square")
    tester(3000, "square")
    tester(4000, "square")
    tester(5000, "square")
    tester(6000, "square")
    tester(7000, "square")
    tester(8000, "square")
    tester(9000, "square")
    tester(10000, "square")
    tester(11000, "square")
    tester(12000, "square")
    tester(13000, "square")
    tester(14000, "square")
    tester(15000, "square")
    tester(16000, "square")
    tester(17000, "square")
    tester(18000, "square")
    tester(19000, "square")
    tester(20000, "square")

    # Test Circle
    tester(1000, "circle")
    tester(2000, "circle")
    tester(3000, "circle")
    tester(4000, "circle")
    tester(5000, "circle")
    tester(6000, "circle")
    tester(7000, "circle")
    tester(8000, "circle")
    tester(9000, "circle")
    tester(10000, "circle")
    tester(11000, "circle")
    tester(12000, "circle")
    tester(13000, "circle")
    tester(14000, "circle")
    tester(15000, "circle")
    tester(16000, "circle")
    tester(17000, "circle")
    tester(18000, "circle")
    tester(19000, "circle")
    tester(20000, "circle")


if __name__ == '__main__':
    go()
