from project.code import general_functions as fun
from sklearn.manifold import TSNE, MDS
import numpy as np

import project.code.quality_assesment.reconstruction_error as er


class Reduction:

    def __init__(self, method, seed=2, labels=None, plot=True):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
        self.custom_labels = False
        self.labels = labels
        self.seed = seed
        self.method = method
        self.plot = plot

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        if self.custom_labels:
            labels = self.labels
        mat = np.array(mat, dtype=np.float64)
        seed = np.random.RandomState(seed=self.seed)
        # MAGIA
        if self.method == 'sne':
            X = TSNE(n_components=2, random_state=seed, metric='precomputed').fit_transform(mat)
        elif self.method == 'mds':
            embedding = MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                            dissimilarity="precomputed", random_state=seed, n_jobs=1,
                            n_init=1)

            X = embedding.fit_transform(mat)

        if self.plot:
            plt = fun.plot(labels, X)

        plt.savefig(self.path_to_results + 't-sne.png')
        print('Error: ', str(er.error(mat, X)) + '%')

        return X
