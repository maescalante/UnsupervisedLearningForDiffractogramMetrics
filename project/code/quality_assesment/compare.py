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
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class compare():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def intra_inter_class(self, title,points,labels):
        # dst = distance.euclidean(a, b)
        label_dict = fun.create_dictionary(labels)
        scaler = MinMaxScaler()
        scaler.fit(points)
        points= scaler.transform (points)

        dic_intra={}
        dic_inter={}
        average_pos={}
        for key in label_dict:
            lis= label_dict[key]
            tot=0
            av=0
            for j in range (0, len(lis)):
                for k in range (0, len(lis)):
                    tot+= distance.euclidean(points[lis[j]-1],points[lis[k-1]-1])
                av+=points[lis[j]-1]
            average_pos[key]= [number / len(lis) for number in av]
            dic_intra[key]=tot/(len(lis)**2)



       # print(average_pos)

        plt.figure()

        for key in average_pos:
            col = fun.randomColor()
            plt.plot(average_pos[key][0], average_pos[key][1], 'o', c=col, label=key)
            for key2 in average_pos:
               dic_inter[str(key)+"-"+str(key2)]= distance.euclidean(average_pos[key], average_pos[key2])
              #  plt.plot(x,y)
        plt.legend()
        plt.title(title)
        print (dic_intra)
        return (dic_inter, dic_intra)

    def plot_quality(self,inter_mds, intra_mds, inter_tsne, intra_tsne, inter_iso, intra_iso):


        n_groups=7
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.3
        opacity = 0.8

        mds=[]
        tsne=[]
        iso=[]
        for key in intra_mds:

            mds.append(intra_mds[key])
            tsne.append(intra_tsne[key])
            iso.append(intra_iso[key])
        print(iso)
        print(tsne)
        print(mds)
        rects1 = plt.bar(index , mds, bar_width,
                         alpha=opacity,
                         color='b',
                         label='MDS')
        rects2 = plt.bar(index+bar_width, tsne, bar_width,
                         alpha=opacity,
                         color='g',
                         label='TSNE')
        rects3 = plt.bar(index+2*bar_width, iso, bar_width,
                         alpha=opacity,
                         color='r',
                         label='ISO')
        plt.xlabel('Clase')
        plt.ylabel('Distancia Intra-Clase')
        plt.title('Distancia Intra Clase')
        #plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
        plt.legend()

        plt.tight_layout()
        plt.show()



    def run(self):

        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)
        ti = fun.to_distance_matrix(mat)

        mds=mds_corrected.main(0)
        tsne= t_sne.main(0)
        iso=isomap.main(0)


        #data= np.concatenate((mds, iso))
        #data = np.concatenate((data, tsne))

        inter_mds, intra_mds=self.intra_inter_class("mds",mds,labels)
        inter_tsne, intra_tsne= self.intra_inter_class("tsne",tsne, labels)
        inter_iso, intra_iso=self.intra_inter_class("isomap",iso, labels)

        self.plot_quality(inter_mds, intra_mds, inter_tsne, intra_tsne, inter_iso, intra_iso)

        Qmds = coranking.coranking_matrix(ti, mds)
        Qtsne = coranking.coranking_matrix(mat, tsne)
        Qiso = coranking.coranking_matrix(mat, iso)

        lcm_mds = coranking.metrics.LCMC(Qmds, 1, 50)
        lcm_tsne = coranking.metrics.LCMC(Qtsne, 1, 50)
        lcm_iso = coranking.metrics.LCMC(Qiso, 1, 50)
        fig, ax = plt.subplots(1, 3)
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
        """
        print("max K Trustworthiness")
        print("    MDS:"+ str(np.argmax(t_mds)))
        print("    tsne:"+ str(np.argmax(t_tsne)))
        print("    isomap:"+ str(np.argmax(t_iso)))

        print("max K Continuity")
        print("    MDS:"+ str(np.argmax(c_mds)))
        print("    tsne:"+ str(np.argmax(c_tsne)))
        print("    isomap:"+ str(np.argmax(c_iso)))
              """
def main():
    comp = compare()
    comp.run()