import matplotlib.pyplot as plt
class dt():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def triangle_inequality(self, mat):
        tc = True
        lab = []
        cont = 0
        total = 0
        # triangle constant, 0 if metric
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                for k in range(0, len(mat)):

                    if mat[i][j] + mat[j][k] < mat[i][k]:

                        tc = False
                        cont = cont + 1

                    total += 1
        if cont == 0:
            print("Triangle inequality " + str(tc) + " porcentaje que no cumplen=" + str("0%"))
        else:
            total_t = len(mat) * (len(mat) - 1) * (len(mat) - 2) / 2
            print("Triangle inequality " + str(tc) + " porcentaje que no cumplen=" + str(
                round(cont / total_t * 100, 5)) + "%")

    def run(self):
        mat=[[0,3,9],
             [3,0,1],
             [9,1,0]]





        plt.show()

        self.triangle_inequality(mat)

def main():
    des_triang = dt()
    des_triang.run()
