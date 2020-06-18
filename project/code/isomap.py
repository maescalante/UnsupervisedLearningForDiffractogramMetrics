from project.code import GeneralFunctions as fun
from sklearn.manifold import Isomap
import numpy as np


class ISOMAP():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        embedding = Isomap(n_components=2)

        X_transformed = embedding.fit_transform(mat)


        plt = fun.plot(labels, X_transformed)

        plt.savefig(self.path_to_results + 'isomap.png')


def main():
    iso = ISOMAP()
    iso.run()