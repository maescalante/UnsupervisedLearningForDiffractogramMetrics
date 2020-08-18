from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np


class Mds():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = fun.diag_zeros(mat)
        mat = np.array(mat, dtype=np.float64)


        seed = np.random.RandomState(seed=3)
        seed3d = np.random.RandomState(seed=5)
        embedding = MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=seed, n_jobs=1,
                    n_init=1)

        X_transformed = embedding.fit_transform(mat)

        print(len(X_transformed))

        print(len(X_transformed[0]))

        plt = fun.plot(labels, X_transformed)
        plt.savefig(self.path_to_results + 'mds.png')

        print('Error: ', str(fun.error(mat, X_transformed)) + '%')

        embedding3d = MDS(n_components=3, dissimilarity='precomputed', random_state=seed3d, metric=False)
        X_transformed3d = embedding3d.fit_transform(mat)
        plt3d = fun.plot(labels, X_transformed3d, components=3)
        plt3d.savefig(self.path_to_results + 'mds3D.png')
        print('Error: ', str(fun.error(mat, X_transformed3d, components=3)) + '%')


def main():
    mds = Mds()
    mds.run()
