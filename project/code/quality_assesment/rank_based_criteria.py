

import matplotlib.pyplot as plt
from scipy.spatial import distance

import numpy as np



def coranking_matrix(high_data_distance_mat, low_data_points):
 
    n, m = high_data_distance_mat.shape
    high_distance = high_data_distance_mat
    low_distance = distance.squareform(distance.pdist(low_data_points))

    high_ranking = high_distance.argsort(axis=1).argsort(axis=1)
    low_ranking = low_distance.argsort(axis=1).argsort(axis=1)

    Q, xedges, yedges = np.histogram2d(high_ranking.flatten(),
                                       low_ranking.flatten(),
                                       bins=n)

    Q = Q[1:, 1:]  # remove rankings which correspond to themselves
    return Q