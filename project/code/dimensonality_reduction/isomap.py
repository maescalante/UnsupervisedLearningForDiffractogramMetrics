from project.code import general_functions as fun
from sklearn.manifold import Isomap
import numpy as np


class ISOMAP():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        seed = np.random.RandomState(seed=1)
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        embedding = Isomap(n_neighbors=16, n_components=2, metric='precomputed')

        X_transformed = embedding.fit_transform(mat)

        plt = fun.plot(labels, X_transformed)

        plt.savefig(self.path_to_results + 'isomap.png')
        print('Error: ', str(fun.error(mat, X_transformed)) + '%')

        embedding3d = Isomap(n_components=3)
        X_transformed3d = embedding3d.fit_transform(mat)
        plt3d = fun.plot(labels, X_transformed3d, components=3)
        plt3d.savefig(self.path_to_results + 'isomap3D.png')
        print('Error: ', str(fun.error_3d(mat, X_transformed3d)) + '%')


def main():
    iso = ISOMAP()
    iso.run()
