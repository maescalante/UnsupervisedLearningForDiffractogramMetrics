from project.code import GeneralFunctions as fun
from sklearn.manifold import TSNE


class Sne():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)

        label_dict = fun.create_dictionary(labels)

        X_embedded = TSNE(n_components=2).fit_transform(mat)

        plt = fun.plot(label_dict, X_embedded)
        plt.savefig(self.path_to_results + 't-sne.png')


def main():
    sne = Sne()
    sne.run()