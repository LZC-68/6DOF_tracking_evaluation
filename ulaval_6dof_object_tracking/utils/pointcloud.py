import numpy as np
from scipy.spatial import ConvexHull, distance_matrix


# def maximum_width(points):
#     hull = ConvexHull(points)
#     hull_points = points[hull.vertices]
#     distances = distance_matrix(hull_points, hull_points)
#     max_width = np.max(distances)
#     return max_width

def maximum_width(points):
    hull = ConvexHull(points[:, 0:3])
    hull_points = points[hull.vertices][:, 0:3]
    distances = distance_matrix(hull_points, hull_points)
    max_width = np.max(distances)
    return max_width
