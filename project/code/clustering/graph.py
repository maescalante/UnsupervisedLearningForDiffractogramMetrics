import networkx as nx
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from project.code import general_functions

class Graph:

    def __init__(self, labels):
        self.g = nx.Graph()
        self.labels = labels
        self.path_to_results = 'project/results/'

    def get_closest_neighbors(self, dis):
        ant = 0
        menores = []
        for k in range(10):
            min = 12345678
            for j in range(len(dis)):
                if ant < dis[j] < min:
                    min = dis[j]
                    menor = j
            ant = dis[menor]
            menores.append(menor)
        return menores

    def plot(self, show):
        val_map = {'Ag2Se': 3,
                   'AgSe': 2.5,
                   'Cu2Se': 2,
                   'CuSe': 1.5,
                   'Ti': 1,
                   'TiN': 0.5,
                   'Si': 0}

        values = [val_map.get(self.g.nodes[i]['className'].split(".")[0]) for i in range(len(self.g.nodes()))]

        plt.subplot(111)
        nx.draw(self.g, node_color=values, font_color='white')
        plt.legend(handles=[
            mpatches.Patch(color='yellow', label='label 1'),
            mpatches.Patch(color='green', label='label 2'),
            mpatches.Patch(color='blue', label='label 3'),
            mpatches.Patch(color='red', label='label 4'),
            mpatches.Patch(color='purple', label='label 5'),
            mpatches.Patch(color='grey', label='label 6'),
            mpatches.Patch(color='orange', label='label 7')])
        plt.savefig(self.path_to_results + 'graph.png')
        if show:
            plt.show()

    def generate(self, mat, normalized=False, show=False):
        if normalized:
            mat = general_functions.to_distance_matrix(mat)
        labels_new = self.labels[1:]
        self.g.add_nodes_from([(i, {"className": labels_new[i]}) for i in range(len(labels_new))])
        for i in range(len(mat)):
            distances = mat[i]
            menores = self.get_closest_neighbors(distances)
            for j in menores:
                if i != j:
                    self.g.add_edge(i, j, weight=mat[i][j] * 5)

        self.plot(show)
