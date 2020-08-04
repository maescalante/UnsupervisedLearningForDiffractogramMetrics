from project.code import general_functions as fun
from sklearn.cluster import KMeans
import numpy as np
from sklearn.manifold import MDS

class Kmeans:

    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
        self.clusters = 7

    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        mat = np.array(mat, dtype=np.float64)

        kmeans = KMeans(n_clusters=self.clusters).fit(mat)
        centroids = kmeans.cluster_centers_

        d = {}
        for i in range(self.clusters):
            d[i] = 0
        for k in kmeans.labels_:
            d[k] += 1

        seed = np.random.RandomState(seed=3)
        embedding = MDS(n_components=2, dissimilarity='precomputed', random_state=seed)

        X_transformed = embedding.fit_transform(mat)

        plt = fun.plot2(kmeans.labels_, X_transformed)
        plt.savefig(self.path_to_results + 'mds_kmeans.png')
        print('Error: ', str(fun.error(mat, X_transformed)) + '%')


def main():
    kmeans = Kmeans()
    kmeans.run()