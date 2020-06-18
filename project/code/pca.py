from sklearn.decomposition import PCA
import numpy as np
from project.code import GeneralFunctions as fun


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
        print('Error: ', str(fun.error(mat, principalComponents)) + '%')

def main():
    pca = Pca()
    pca.run()