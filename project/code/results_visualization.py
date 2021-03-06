from project.code import general_functions as fun
import numpy as np
import matplotlib.pyplot as plt
from project.code.dimensonality_reduction.Reduction import Reduction
from project.code.clustering import hierarchical, k_medoids
from project.code.clustering.graph import Graph
from sklearn import metrics


class results:

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        # Visualización 0 creacion de un grafo para observar las agrupaciones
        Graph(labels).generate(mat, normalized=True, show=True)

        #Visualización 6 hierarchical

        hierarchical.Hierarchical().run()

        [medoids, map, cost] = k_medoids.Kmedoids().run(mat)
        #Reduction(method='sne', seed=3, labels=medoids).run()
        labels_pred = []
        for item in map:
            elemento = labels[map[item]].split(".")
            labels_pred.append(elemento[0])
        new_labels = []
        for i in range(len(labels)):
            if i!=0:
                elemento = labels[i].split(".")
                new_labels.append(elemento[0])

        print(metrics.adjusted_rand_score(new_labels, labels_pred))
        print(metrics.homogeneity_score(new_labels, labels_pred))
        print(metrics.completeness_score(new_labels, labels_pred))
        print(metrics.v_measure_score(new_labels, labels_pred))

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


def main():
    r = results()
    r.run()
