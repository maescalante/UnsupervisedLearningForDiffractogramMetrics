from project.code import GeneralFunctions as fun
from sklearn.manifold import MDS
import numpy as np


class Mds():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        seed = np.random.RandomState(seed=6)
        embedding = MDS(n_components=2, dissimilarity='precomputed', random_state=seed)
        X_transformed = embedding.fit_transform(mat)

        dic = fun.create_dictionary(labels)

        plt = fun.plot(dic, X_transformed)

        plt.savefig(self.path_to_results + 'mds.png')


def main():
    mds = Mds()
    mds.run()