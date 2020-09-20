from project.code import general_functions as fun
from sklearn.manifold import Isomap
import numpy as np
import project.code.quality_assesment.reconstruction_error as er


class ISOMAP():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self,plot_flag=1):
        seed = np.random.RandomState(seed=1)
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        embedding = Isomap(n_neighbors=91, n_components=14, metric='precomputed')

        X_transformed = embedding.fit_transform(mat)
        if plot_flag==1:
            plt = fun.plot(labels, X_transformed)

            plt.savefig(self.path_to_results + 'isomap.png')
        print('Error ISOMAP 2D: ', str(er.error(mat, X_transformed)) + '%')

        embedding3d = Isomap(n_components=3)
        X_transformed3d = embedding3d.fit_transform(mat)
        if plot_flag==1:
            plt3d = fun.plot(labels, X_transformed3d, components=3)
            plt3d.savefig(self.path_to_results + 'isomap3D.png')
        print('Error ISOMAP 3D: ', str(er.error(mat, X_transformed3d, components=3)) + '%')
        return X_transformed

def main(plot_flag=1):
    iso = ISOMAP()
    resp=iso.run(plot_flag)
    return resp
