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
from project.code.dimensonality_reduction import mds_corrected
from project.code.dimensonality_reduction import t_sne
from project.code.dimensonality_reduction import isomap

class compare():

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
        ti = fun.to_distance_matrix(mat)

        mds=mds_corrected.main()
        tsne= t_sne.main()
        
        Q = coranking.coranking_matrix(ti, X_transformed)

        print(Q)

        lcm = coranking.metrics.LCMC(Q, 1, 50)
        plt.plot(lcm)





def main():
    comp = compare()
    comp.run()