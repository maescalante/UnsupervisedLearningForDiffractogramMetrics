from project.code import general_functions as fun

from sklearn.manifold import TSNE
import numpy as np
import project.code.quality_assesment.reconstruction_error as er
class Sne():

    def __init__(self, labels = None):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
        self.custom_labels = False
        self.labels = labels

    def run(self, plot_flag=1):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        if self.custom_labels:
            labels = self.labels
        mat = np.array(mat, dtype=np.float64)
        seed = np.random.RandomState(seed=2)
        X_embedded = TSNE(n_components=2, random_state=seed, metric='precomputed').fit_transform(mat)
        # X_embedded = SNE_RAW().fit(mat)
        if plot_flag==1:
            plt = fun.plot(labels, X_embedded)

            plt.savefig(self.path_to_results + 't-sne.png')

        print('Error TSNE 2D: ', str(er.error(mat, X_embedded)) + '%')


        seed3d = np.random.RandomState(seed=5)
        embedding3d = TSNE(n_components=3, random_state=seed3d, metric='precomputed')
        X_transformed3d = embedding3d.fit_transform(mat)
        if plot_flag==1:
            plt3d = fun.plot(labels, X_transformed3d, components=3)
            plt3d.savefig(self.path_to_results + 't-sne3D.png')
        print('Error TSNE 3D: ', str(er.error(mat, X_transformed3d, components=3)) + '%')
        return X_embedded
def main(plot_flag=1):
    sne = Sne()
    resp=sne.run(plot_flag)
    return resp