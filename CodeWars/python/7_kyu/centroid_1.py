# https://www.codewars.com/kata/58811e9cfd05cb5aed0000a4/train/python

def centroid(points: list[list[float]]) -> list[float]:
    output = [0.0, 0.0, 0.0]
    for point in points:
        output[0] += point[0]
        output[1] += point[1]
        output[2] += point[2]
    output[0] /= len(points)
    output[1] /= len(points)
    output[2] /= len(points)
    return output
