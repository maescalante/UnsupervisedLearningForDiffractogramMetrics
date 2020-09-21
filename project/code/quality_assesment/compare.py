from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
from scipy.spatial import distance
import coranking
import matplotlib.pyplot as plt
import math
from coranking.metrics import trustworthiness
from coranking.metrics import continuity
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
        fig,ax=plt.subplots(1,3)
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)
        ti = fun.to_distance_matrix(mat)

        mds=mds_corrected.main(0)
        tsne= t_sne.main(0)
        iso=isomap.main(0)

        Qmds = coranking.coranking_matrix(ti, mds)
        Qtsne = coranking.coranking_matrix(mat, tsne)
        Qiso = coranking.coranking_matrix(mat, iso)

        lcm_mds = coranking.metrics.LCMC(Qmds, 1, 50)
        lcm_tsne = coranking.metrics.LCMC(Qtsne, 1, 50)
        lcm_iso = coranking.metrics.LCMC(Qiso, 1, 50)
        ax[0].set_title("LCMC")
        ax[0].set(xlabel='K', ylabel='LCMC')
        ax[0].plot(lcm_mds)
        ax[0].plot(lcm_tsne)
        ax[0].plot(lcm_iso)
        ax[0].legend(["MDS", "TSNE", "ISOMAP"])
        #plt.show()



        t_mds = trustworthiness(Qmds,1,50)
        t_tsne = trustworthiness(Qtsne, 1, 50)
        t_iso = trustworthiness(Qiso, 1, 50)
        ax[1].set_title("Trustworthiness")
        ax[1].set(xlabel='K', ylabel='Trustworthiness')
        ax[1].plot(t_mds)
        ax[1].plot(t_tsne)
        ax[1].plot(t_iso)
        ax[1].legend(["MDS", "TSNE", "ISOMAP"])

        c_mds = continuity(Qmds, 1, 50)
        c_tsne = continuity(Qtsne, 1, 50)
        c_iso = continuity(Qiso, 1, 50)
        ax[2].set_title("Continuity")
        ax[2].set(xlabel='K', ylabel='Continuity')
        ax[2].plot(c_mds)
        ax[2].plot(c_tsne)
        ax[2].plot(c_iso)
        ax[2].legend(["MDS", "TSNE", "ISOMAP"])


        plt.show()

        print("max K LCMC")
        print("    MDS:"+ str(np.argmax(lcm_mds)))
        print("    tsne:"+ str(np.argmax(lcm_tsne)))
        print("    isomap:"+ str(np.argmax(lcm_iso)))

        print("max K Trustworthiness")
        print("    MDS:"+ str(np.argmax(t_mds)))
        print("    tsne:"+ str(np.argmax(t_tsne)))
        print("    isomap:"+ str(np.argmax(t_iso)))

        print("max K Continuity")
        print("    MDS:"+ str(np.argmax(c_mds)))
        print("    tsne:"+ str(np.argmax(c_tsne)))
        print("    isomap:"+ str(np.argmax(c_iso)))

def main():
    comp = compare()
    comp.run()