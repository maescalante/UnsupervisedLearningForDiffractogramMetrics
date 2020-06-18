from project.code import GeneralFunctions as fun
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
        seed = np.random.RandomState(seed=5)
        X_embedded = TSNE(n_components=2, random_state=seed).fit_transform(mat)
        plt = fun.plot(labels, X_embedded)


        plt.savefig(self.path_to_results + 't-sne.png')


        print('Error: ', str(fun.error(mat, X_embedded)) + '%')


def main():
    sne = Sne()
    sne.run()
