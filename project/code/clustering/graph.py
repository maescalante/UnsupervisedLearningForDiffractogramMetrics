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
            mpatches.Patch(color='#FDE725', label='Ag2Se'),
            mpatches.Patch(color='#440154', label='Si'),
            mpatches.Patch(color='#35B779', label='Cu2Se'),
            mpatches.Patch(color='#21918C', label='CuSe'),
            mpatches.Patch(color='#90D743', label='AgSe'),
            mpatches.Patch(color='#31688E', label='Ti'),
            mpatches.Patch(color='#443983', label='TiN')])
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
