import numpy as np
from project.code.clustering.KMedoids import KMedoids


class Kmedoids:

    def __init__(self, clusters=7):
        self.clusters = clusters

    def run(self, mat):
        mat = np.array(mat, dtype=np.float64)
        return KMedoids(medoids=self.clusters).fit(mat)
