from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
import scipy.linalg as la
from numpy.linalg import matrix_power
import scipy.optimize._minimize as opti
import math
import project.code.quality_assesment.reconstruction_error as er
class mds_raw():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'


    def triangle_inequality(self, mat, labels):
        tc = True
        lab=[]
        cont=0
        total=0
        # triangle constant, 0 if metric
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                for k in range(0, len(mat)):

                    if mat[i][j]+mat[j][k]<mat[i][k]:

                        tc=False
                        cont=cont+1
                        if labels[i] not in lab:

                            lab.append(labels[i])
                    total+=1
        if cont==0:
            print("Triangle inequality " + str(tc) + " porcentaje que no cumplen=" + str("0%"))
        else:
            total_t= len(mat)*(len(mat)-1)*(len(mat)-2)/2
            print("Triangle inequality " + str(tc)+ " porcentaje que no cumplen="+str(round(cont/total_t*100,5))+"%")




    def const_c(self, mat):

        maxi = 0
        # triangle constant, 0 if metric
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                for k in range(0, len(mat)):
                    val=abs(mat[i][j] - mat[i][k] + mat[j][k])
                    if val>maxi:
                        maxi=val
        return maxi




    #input is a matrix that does not satisfy the traingle inequality
    def to_distance_matrix(self, dissimilarity_mat):
        N= len(dissimilarity_mat)
        e=[[0 for i in range(N)] for j in range(N)]
        z=[[[0 for i in range(N)] for j in range(N)] for k in range(N)]

        eps=10^-3
        delta=1+eps
        while delta>eps:
            e_act=e
            for i in range (0,N):
                for j in range (0,N):
                    for k in range (0,N):
                        b=dissimilarity_mat[k][i]+dissimilarity_mat[j][k]+dissimilarity_mat[i][j]

                        u=-1/3 * (b-e[i][j]+e[j][k]+e[k][i])

                        theta=min(u,z[i][j][k])

                        e[i][j]=e[i][j]+theta
                        e[j][k]=e[j][k]-theta
                        e[k][i]=e[k][i]-theta

                        z[i][j][k]=z[i][j][k]+theta
            dif=np.subtract(e,e_act)
            delta=np.sum(dif)

        return dissimilarity_mat+e

    def to_distance_matrix2(self, dissimilarity_mat, c):
        N=len(dissimilarity_mat)
        for i in range(0,N):
            for j in range(0,N):
                if i==j:
                    dissimilarity_mat[i][j]=0
                else:
                    dissimilarity_mat[i][j]=dissimilarity_mat[i][j]+c
        return dissimilarity_mat

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

        self.triangle_inequality(mat,labels)

        c=self.const_c(mat)
        ti=self.to_distance_matrix2(mat,c)

        self.triangle_inequality(ti,labels)

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


def main():
    mds = mds_raw()
    mds.run()