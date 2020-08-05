from project.code import general_functions as fun
from project.code.dimensonality_reduction.sne_raw import SNE_RAW
from sklearn.manifold import TSNE
import numpy as np


class Sne():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)
        seed = np.random.RandomState(seed=2)
        X_embedded = TSNE(n_components=2, random_state=seed, metric='precomputed').fit_transform(mat)
        # X_embedded = SNE_RAW().fit(mat)
        plt = fun.plot(labels, X_embedded)

        plt.savefig(self.path_to_results + 't-sne.png')

        print('Error: ', str(fun.error(mat, X_embedded)) + '%')

        seed3d = np.random.RandomState(seed=5)
        embedding3d = TSNE(n_components=3, random_state=seed3d, metric='precomputed')
        X_transformed3d = embedding3d.fit_transform(mat)
        plt3d = fun.plot(labels, X_transformed3d, components=3)
        plt3d.savefig(self.path_to_results + 't-sne3D.png')
        print('Error3D: ', str(fun.error(mat, X_transformed3d, components=3)) + '%')


def main():
    sne = Sne()
    sne.run()
