from sklearn.decomposition import PCA
import numpy as np
from project.code import general_functions as fun
import project.code.quality_assesment.reconstruction_error as er


class Pca():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(mat)

        plt = fun.plot(labels, principalComponents)

        plt.savefig(self.path_to_results + 'pca.png')
        print('Error: ', str(er.error(mat, principalComponents)) + '%')

        seed3d = np.random.RandomState(seed=5)
        embedding3d = PCA(n_components=3, random_state=seed3d)
        X_transformed3d = embedding3d.fit_transform(mat)
        plt3d = fun.plot(labels, X_transformed3d, components=3)
        plt3d.savefig(self.path_to_results + 'pca3D.png')
        print('Error: ', str(er.error(mat, X_transformed3d, components=3)) + '%')


def main():
    pca = Pca()
    pca.run()
