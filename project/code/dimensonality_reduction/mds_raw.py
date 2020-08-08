from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
import scipy.linalg as la
from numpy.linalg import matrix_power
import scipy.optimize._minimize as opti
import math

class mds_raw():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
    def triangle_inequality(self, mat):
        tc = True
        cont=0
        total=0
        # triangle constant, 0 if metric
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                for k in range(0, len(mat)):

                    if mat[i][j]+mat[j][k]<mat[i][k]:

                        tc=False
                        cont=cont+1
                    total+=1
        if cont==0:
            print("Triangle inequality " + str(tc) + " porcentaje que no cumplen=" + str("0%"))
        else:
            total_t= len(mat)*(len(mat)-1)*(len(mat)-2)/2
            print("Triangle inequality " + str(tc)+ " porcentaje que no cumplen="+str(round(cont/total_t*100,5))+"%")


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
                        b=dissimilarity_mat[k][i]+dissimilarity_mat[j][k]-dissimilarity_mat[i][j]

                        u=-1/3 * (b-e[i][j]+e[j][k]+e[k][i])

                        theta=min(u,z[i][j][k])

                        e[i][j]=e[i][j]+theta
                        e[j][k]=e[j][k]-theta
                        e[k][i]=e[k][i]-theta

                        z[i][j][k]=z[i][j][k]+theta
            dif=np.subtract(e,e_act)
            delta=np.sum(dif)

        return dissimilarity_mat+e

    def to_distance_matrix2(self, dissimilarity_mat):
        N= len(dissimilarity_mat)
        iters=100
        i=0
        e=10^-3
        w = [[1 for j in range(N)] for k in range(N)]
        while i<iters:
            p_new=opti(self.to_minimize(w,self.perturbation(dissimilarity_mat)))
            w=1/(p_new+e)
            i=i+1
    def to_minimize(self,w, p):
        N = len(p)
        sum=0
        for i in range (0,N):
            for j in range(0,N):
                sum=sum+w[i][j]*np.abs(p)
    def perturbation(self,D):
        ori=D
        N = len(D)
        for i in range(0, N):
            for j in range(0, N):
                for k in range(0, N):
                    if D[i][j]>=D[i][k]+D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
        return np.subtract(ori,D)
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

        self.triangle_inequality(mat)

        prueba=[[0,16,47,72,77,79],
                [16,0,37,57,65,66],
                [47,37,0,40,30,35],
                [72,57,40,0,31,23],
                [77,65,30,31,0,10],
                [79,66,35,23,10,0]]
        prueba2=[[0,4],
                 [4,0]]
        self.triangle_inequality(prueba2)
        self.triangle_inequality(prueba)
        #lamp=la.eig(prueba)
        #self.nef(lamp[0])
        #mat=np.square(mat)

        #n=len(mat)
        #m=2
        #Z= np.identity(n)- (1/n)*np.ones(n)

        #B=-1/2*np.dot(np.dot(Z,mat),Z)

        #results = la.eig(B)
        #Q=results[1]

        #Q=Q[:,0:m]


        #lam=results[0]
        #self.nef(lam)



        #lam=lam[0:m]*np.identity(m)

        #hay eingenvalues negativos porque no se usan distancias euclidianas
        #print(lam)
        #X_transformed=np.dot(Q,matrix_power(lam,-1))

        #X_transformed=np.int_(X_transformed.real)

        #print((X_transformed))


        #plt = fun.plot(labels, X_transformed)
        #plt.savefig(self.path_to_results + 'mds_raw.png')


        #print('Error: ', str(fun.error(mat, X_transformed)) + '%')
        corrected=fun.diag_zeros(mat)
        self.triangle_inequality(corrected)
        ti=self.to_distance_matrix(prueba)

        #self.triangle_inequality(ti)
        print(ti)
        seed = np.random.RandomState(seed=3)
        seed3d = np.random.RandomState(seed=5)
        embedding = MDS(n_components=2, dissimilarity='precomputed', random_state=seed, metric=True)

        X_transformed = embedding.fit_transform(ti)
        plt = fun.plot(labels, X_transformed)
        plt.savefig(self.path_to_results + 'mdsMetric.png')

        print('Error: ', str(fun.error(ti, X_transformed)) + '%')



def main():
    mds = mds_raw()
    mds.run()