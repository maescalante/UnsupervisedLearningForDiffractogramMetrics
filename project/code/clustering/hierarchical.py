from project.code import general_functions as fun
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt


class Hierarchical:

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def plot_dendrogram(self, model, labels, **kwargs):
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

        fig = plt.figure()
        fig.suptitle('Hierarchical Clustering Dendrogram', fontsize=20, fontweight="bold")
        #plt.title('Hierarchical Clustering Dendrogram', labelsize=20)
        ax = fig.add_subplot(1, 1, 1)
        dendrogram(linkage_matrix, **kwargs, labels=labels, ax=ax)
        ax.tick_params(axis='x', which='major', labelsize=15)
        fig.savefig('t.png')
        plt.yticks([])
        plt.xlabel("Number of points in node (or index of point if no parenthesis).", fontsize=20)

        plt.savefig(self.path_to_results + 'hierarchical.png', dpi=300)
        plt.show()


    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        X = np.array(mat, dtype=np.float64)

        # setting distance_threshold=0 ensures we compute the full tree.
        model = AgglomerativeClustering(n_clusters=None, affinity="precomputed", linkage="average",
                                        distance_threshold=0)

        model = model.fit(X)

        # plot the top three levels of the dendrogram
        self.plot_dendrogram(model, labels, truncate_mode='level', p=7)
