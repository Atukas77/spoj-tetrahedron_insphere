"""
A program that takes in six sides of a tetrahedron and calculates the radius
of a sphere that fits inside of it.
"""

import numpy as np
import math 

def triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def face_areas(sides):
    a, b, c, d, e, f = sides
    
    # Calculate the area of each face
    face1 = triangle_area(a, b, d)  # WX, WY, XY
    face2 = triangle_area(a, c, e)  # WX, WZ, XZ
    face3 = triangle_area(b, c, f)  # WY, WZ, YZ
    face4 = triangle_area(d, e, f)  # XY, XZ, YZ
    
    return face1, face2, face3, face4

def volume(sides):
    a, b, c, d, e, f = sides
    
    # Construct the Cayley-Menger matrix
    CM = np.array([
        [0,   1,    1,    1,    1],
        [1,   0, a**2, b**2, c**2],
        [1, a**2,   0, d**2, e**2],
        [1, b**2, d**2,   0, f**2],
        [1, c**2, e**2, f**2,   0]
    ])
    
    # Calculate the determinant of the matrix
    det_CM = np.linalg.det(CM)
    
    # Compute the volume squared
    volume_squared = det_CM / 288
    
    # Take the square root to get the volume
    volume = np.sqrt(volume_squared) if volume_squared > 0 else 0
    
    return volume


n = int(input())
sides = []

for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    sides.append((a, b, c, d, e, f))

for i in range(n):
    v = volume(sides[i])
    r = 3*v/(sum(face_areas(sides[i])))
    print(f"{r:.4f}")