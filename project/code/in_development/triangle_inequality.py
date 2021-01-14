from project.code import general_functions as fun


class dt():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat = [[0, 3, 9],
               [3, 0, 1],
               [9, 1, 0]]
        print(fun.const_c(mat))

        mat2 = fun.to_distance_matrix(mat)
        print(mat2)


def main():
    des_triang = dt()
    des_triang.run()
