from project.code import GeneralFunctions as fun
from sklearn.manifold import MDS
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy

def plot_dendrogram(model,labels, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs, labels=labels)


class Mds():

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        X = np.array(mat, dtype=np.float64)


        # setting distance_threshold=0 ensures we compute the full tree.
        model = AgglomerativeClustering(n_clusters=None,distance_threshold=0)

        model = model.fit(X)

        plt.title('Hierarchical Clustering Dendrogram')
        # plot the top three levels of the dendrogram
        plot_dendrogram(model, labels,truncate_mode='level', p=7)
        plt.xlabel("Number of points in node (or index of point if no parenthesis).")

        plt.show()



def main():
    mds = Mds()
    mds.run()

