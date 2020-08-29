from project.code import general_functions as fun
import numpy as np
from sklearn.manifold import MDS
from project.code.clustering.KMedoids import KMedoids


class Kmedoids:

    def __init__(self, ):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
        self.clusters = 7

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        return KMedoids(medoids=7).fit(mat)
