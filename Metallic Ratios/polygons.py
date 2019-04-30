# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:29:46 2018

@author: NathanLHall
"""

import matplotlib.pyplot as plt
from sympy import cos, sin, pi, solve, sqrt
from sympy.abc import x
from sympy.geometry import Point
#import sympy.geometry.point

# Number of sides = number of vertices; Used interchangably, but the vertex is the point
# of interest to find coordinate point.
def coords(vertices, angle):

    points = []
    if vertices % 4 == 0:
        for i in range(vertices):
            x = cos(i * angle + pi / 4)
            y = sin(i * angle + pi / 4)
            points.append(Point(x, y))
        return(points)
    else:
        for i in range(vertices):
            x = cos(i * angle + pi / 2)
            y = sin(i * angle + pi / 2)
            points.append(Point(x, y))
        return(points)

def normalize_edges(points):
    edge_length = points[0].distance(points[1])

    normalized_points = []
    for point in points:
        point = Point(point[0] / edge_length, point[1] / edge_length)
        normalized_points.append(point)
    return normalized_points

if __name__ == "__main__":

    ratios = solve(x**2 -1*x -1, x)
    sides = int(input("Input number of sides: "))
    interior_angle = 2 * pi / sides

    points = coords(sides, interior_angle)
#    points = normalize_edges(points)

#    for point in points:
#        print(point)
#    print()


    edge_length = points[0].distance(points[1])
    print(edge_length)

    xn = []
    yn = []
    for point in points:
        xn.append(point[0])
        yn.append(point[1])

    plt.plot(xn, yn, 'o', markersize = 5, color='k')
    plt.plot(xn[0], yn[0], 'o', markersize = 5, color='r')
    plt.axis('equal')

    phi = solve(x**2 - x - 1, x)
    diagonal = points[0].distance(points[2])

    print("Edge:", edge_length)
    print("Diagonal:", diagonal)
    print("Ratio:", diagonal/edge_length)