from project.code import general_functions as fun
from sklearn.manifold import MDS
import numpy as np
import scipy.linalg as la
from numpy.linalg import matrix_power

class mds_raw():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        mat=np.square(mat)

        n=len(mat)
        m=2
        Z= np.identity(n)- (1/n)*np.ones(n)

        B=-1/2*np.dot(np.dot(Z,mat),Z)

        results = la.eig(B)
        Q=results[1]

        Q=Q[:,0:m]


        lam=results[0]

        lam=lam[0:m]*np.identity(m)
        #hay eingenvalues negativos porque no se usan distancias euclidianas
        print(lam)
        X_transformed=np.dot(Q,matrix_power(lam,-1))

        #X_transformed=np.int_(X_transformed.real)

        #print((X_transformed))


        plt = fun.plot(labels, X_transformed)
        plt.savefig(self.path_to_results + 'mds_raw.png')


        print('Error: ', str(fun.error(mat, X_transformed)) + '%')




def main():
    mds = mds_raw()
    mds.run()