from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
from scipy.spatial import distance
import coranking
import matplotlib.pyplot as plt

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


    def run(self):

        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)
        ti = fun.to_distance_matrix(mat)

        mds=mds_corrected.main()
        tsne= t_sne.main()
        iso=isomap.main()

        Qmds = coranking.coranking_matrix(ti, mds)
        Qtsne = coranking.coranking_matrix(mat, tsne)
        Qiso = coranking.coranking_matrix(mat, iso)


        lcm_mds = coranking.metrics.LCMC(Qmds, 1, 50)
        lcm_tsne = coranking.metrics.LCMC(Qtsne, 1, 50)
        lcm_iso = coranking.metrics.LCMC(Qiso, 1, 50)
        plt.plot(lcm_mds)
        plt.plot(lcm_tsne)
        plt.plot(lcm_iso)
        plt.legend(["MDS", "TSNE", "ISOMAP"])
        plt.show()





def main():
    comp = compare()
    comp.run()