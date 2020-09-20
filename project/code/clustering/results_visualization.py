from project.code import general_functions as fun
import numpy as np
import matplotlib.pyplot as plt
from project.code.dimensonality_reduction.Reduction import Reduction
from project.code.clustering import hierarchical, k_medoids


class results:

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        # visualización 1 matriz con mapa de calor
        plt.imshow(mat)
        plt.colorbar()
        plt.show()

        # Visualización 3 mds raw y luego k medoids

        [medoids, map, cost] = k_medoids.Kmedoids().run(mat)
        Reduction(method='sne', seed=2, labels=medoids).run()

        # Visualización 5 t-sne y luego k medoids

        [medoids, map, cost] = k_medoids.Kmedoids().run(mat)
        Reduction(method='mds', seed=3, labels=medoids).run()

        # Visualización 6 hierarchical

        hierarchical.Hierarchical().run()


def main():
    r = results()
    r.run()
