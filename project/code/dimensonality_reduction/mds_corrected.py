from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
from scipy.spatial import distance
import coranking
import matplotlib as plt
from nose import tools as nose
from coranking.metrics import trustworthiness
import project.code.quality_assesment.reconstruction_error as er
import project.code.quality_assesment.rank_based_criteria as rbc
class mds_raw():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'


    def nef(self,lam):
        # negative eige fraction -- the dregree to which the distance matrix departs from being euclidean
        # if nef is 0 metrics are euclidean
        neg = 0
        sum = 0
        for i in lam:
            if i < 0:
                neg = neg + abs(i)
            sum = sum + abs(i)
        NEF = neg / sum
        print("NEF " + str(NEF))

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        fun.triangle_inequality(mat)

        ti=fun.to_distance_matrix(mat)

        fun.triangle_inequality(ti)

        #print(ti)
        seed = np.random.RandomState(seed=5)
        seed3d = np.random.RandomState(seed=4)
        embedding = MDS(n_components=2, dissimilarity='precomputed', random_state=seed, metric=True)

        X_transformed = embedding.fit_transform(ti)
        plt = fun.plot(labels, X_transformed)
        plt.savefig(self.path_to_results + 'mdsMetric.png')


        print('Error: ', str(er.error(ti, X_transformed)) + '%')





        embedding3d = MDS(n_components=3, dissimilarity='precomputed', random_state=seed3d, metric=False)
        X_transformed3d = embedding3d.fit_transform(mat)

        plt3d = fun.plot(labels, X_transformed3d, components=3)
        plt3d.savefig(self.path_to_results + 'mds_raw3D.png')
        print('Error: ', str(er.error(mat, X_transformed3d, components=3)) + '%')
        return X_transformed

def main():
    mds = mds_raw()
    mds.run()